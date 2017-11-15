from django.contrib.auth.models import User
from fair.models import Fair
from exhibitors.models import Exhibitor
from matching.models import *

from student_profiles.models import StudentProfile, MatchingResult

from random import randint
import math
import json
import numpy as np

from django.utils import timezone
import logging

class TempMatchingResult(object):
    '''
    Used to store temporary result data before writing to db
    '''
    def __init__(self):
        self.exhibitor = None
        self.distance = 0
        self.score = 0
        self.common = []

def gen_random_result(student, exhibitor, score, fair):
    '''
    '''
    result = MatchingResult.objects.create(student=student,
        exhibitor=exhibitor,
        fair=fair,
        score=score)

def randomize_answers(student, survey, numberOfResults):
    '''
    Until algorithm is working corretly we write answers to MatchingResult for
    the apps to get some data
    '''
    fair = Fair.objects.get(current=True)
    exhibitors = list(Exhibitor.objects.filter(fair=fair))
    ex_len = len(exhibitors)
    for i in range(numberOfResults):
        if i == 0:
            score = 100
        else:
            score = randint(0,100)
        gen_random_result(student, exhibitors[randint(0,ex_len-1)], score, fair)

def gen_results(student, survey, temp_results, N):
    fair = survey.fair
    max_distance = max([temp.distance for temp in temp_results])
    for result in temp_results:
        result.score -= int( 20 *(1.0 - result.distance/max_distance) * result.score / 90 )
        if result.score < 0:
            result.score = 0

    sorted_temp_result = sorted(temp_results, key=lambda t: t.score, reverse=True)
    for i in range(N):
        temp_res = sorted_temp_result[i]
        MatchingResult.objects.create(
            student=student,
            fair=fair,
            exhibitor = temp_res.exhibitor,
            score = temp_res.score,
            )

def get_similarities_value(student_array, exhibitor_array):
    '''
    Requires both arrays to be numpy arrays
    returns a quotient on how many wrong elements student array has
    '''
    ex_sum = sum(exhibitor_array)
    stud_sum = sum(student_array)
    if (student_array == exhibitor_array).all() is True:
        return 1.0
    else:
        true_count = 0
        for i in range(len(student_array)):
            if student_array[i] == exhibitor_array[i] and student_array[i] == 1:
                true_count += 1
        return float(true_count) / float(stud_sum)


def gen_answers(student, survey, classifier, numberOfResults):
    '''
    Use the KNN classifer to generate results.
    The classifier gives a 90 percent score if the student has all workfields as an exhibitor. The excess workfields can remove up to 10 percent depending on how many extra fields the student has filled in which are not represented in the exhibitor

    for the slider, grading
    '''
    space_dict = classifier.get_dict()
    #key_dict = dict(zip(space_dict.values(), space_dict.keys()))
    student_array = np.zeros(classifier.space_dim)
    student_answers_workfield = StudentAnswerWorkField.objects.filter(student=student, survey=survey)
    for wfield_ans in student_answers_workfield:
        student_array[ space_dict[str(wfield_ans.work_field.pk)] ] = 1

    try:
        norm_fun = eval('%s_norm'%classifier.norm_type)
    except:
        norm_fun = euclidian_norm

    exhibitor_arrays = VectorKNN.objects.filter(classifier=classifier)
    temp_results = [TempMatchingResult]*len(exhibitor_arrays)

    for i, ex_array in enumerate(exhibitor_arrays):
        result = TempMatchingResult()
        result.exhibitor = ex_array.exhibitor
        ex_vector = np.array(ex_array.get_vector())

        result.score = int(90 * get_similarities_value(student_array, ex_vector) )
        result.distance = norm_fun(student_array, ex_vector)
        temp_results[i] = result
    gen_results(student, survey, temp_results, numberOfResults)

def euclidian_norm(array1, array2):
    norm = 0
    for i in range(len(array1)):
        norm += pow(array1[i] - array2[i], 2)
    return pow(norm, 0.5)


def classify(student_id, survey_id, numberOfResults=10):
    '''
    Main classifer to be called from the api when the final put request is called
    from the apps

    required input is
    student_id (pk)         - a primary key to a StudentProfile object
    survey (pk)             - a primary key to the survey used
    numberOfResults (int)   - integer specifying how many results should be
                              generated for the student_id
    '''
    finished_flag = False
    # survey_raw = TODO add relates_to = models.ForeignKey('self') in Survey if nec
    logging_str = ''
    try:
        student = StudentProfile.objects.get(pk=student_id)
        survey = Survey.objects.get(pk=survey_id)
        classifier = KNNClassifier.objects.get(survey=survey, current=True)
        # this is only now to make sure the knn works
        try:
            gen_answers(student, survey, classifier, numberOfResults)
            finished_flag = True
            logging_str = 'Matching Finshed for student %s at %s'%(student.id_string, str(timezone.now()))
        except Exception as e:
            randomize_answers(student, survey, numberOfResults)
            logging_str = 'Failed to run classifier, ran random_answers for student %s : %s'%(student.id_string, str(e))

    except (StudentProfile.DoesNotExist, Survey.DoesNotExist, classifier.DoesNotExist) as e:
        logging_str = 'Failed to run any classifier for student %s : %s'%(str(student.id_string), str(e))

    student.classifier_log = logging_str
    student.save()
    return finished_flag

def init_classifier(survey_id, classifer_type = 'euclidian'):
    '''
    initialization of classifer using KNN only for now and euclidian dist as standard
    '''
    created = False
    survey = Survey.objects.get(pk=survey_id)
    workfields = WorkField.objects.filter(survey=survey)

    try:
        classifier = KNNClassifier.objects.get(survey=survey, current=True)

    except KNNClassifier.DoesNotExist:

        created = True
        space_dim = len(workfields)
        classifier = KNNClassifier.objects.create(survey=survey,
            space_dim=space_dim,
            current=True
        )
        keys = [w.pk for w in workfields]
        positions = list(range(0,space_dim))
        space_dict = dict(zip(keys, positions))
        classifier.set_dict(space_dict)
        classifier.save()

    vectors = VectorKNN.objects.filter(classifier=classifier)
    if not vectors:
        gen_workfield_vectors(classifier, workfields)

    return created

def gen_workfield_vectors(classifier, workfields):
    '''
    generates a workfield vector for each exhibitor for the current classifier
    '''
    exhibitors_all = []
    for wfield in workfields:
        exhibitors_all += wfield.exhibitors.all()
    exhibitors = set(exhibitors_all)
    space_dict = classifier.get_dict()

    for ex in exhibitors:
        array = [0]*classifier.space_dim
        for wfield in workfields:
            if ex in wfield.exhibitors.all():
                array[space_dict[str(wfield.pk)]] = 1

        VectorKNN.objects.create(vector=str(array), classifier=classifier, exhibitor=ex)