from collections import OrderedDict
from datetime import datetime

import platform, subprocess, json

from django.contrib.auth.models import Group
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.cache import cache_page

import api.serializers as serializers, api.deserializers as deserializers

from banquet.models import BanquetteAttendant
from events.models import Event
from exhibitors.models import Exhibitor, CatalogInfo
from fair.models import Partner, Fair
from django.utils import timezone
from matching.models import StudentQuestionBase as QuestionBase, WorkField, Survey
from news.models import NewsArticle
from recruitment.models import RecruitmentPeriod, RecruitmentApplication, Role 
from student_profiles.models import StudentProfile

def root(request):
    return JsonResponse({'message': 'Welcome to the Armada API!'})


@cache_page(60 * 5)
def exhibitors(request):
    '''
    Returns the existing cataloginfo for exhibitors in current fair. 
    Does not return anything for those exhibitors that are without catalog info.
    '''
    fair = Fair.objects.get(current=True)
    exhibitors = Exhibitor.objects.filter(fair=fair)

    data = [serializers.exhibitor(request, exhibitor, exhibitor.company)
            for exhibitor in exhibitors]
    #data.sort(key=lambda x: x['company_name'].lower())
    return JsonResponse(data, safe=False)

@cache_page(60 * 5)
def events(request):
    '''
    Returns all events for this years fair
    '''
    fair = Fair.objects.get(current=True)
    events = Event.objects.filter(published=True, fair=fair)
    data = [serializers.event(request, event) for event in events]
    return JsonResponse(data, safe=False)



@cache_page(60 * 5)
def news(request):
    '''
    Returns all news
    '''
    news = NewsArticle.public_articles.all()
    data = [serializers.newsarticle(request, article) for article in news]
    return JsonResponse(data, safe=False)

@cache_page(60 * 5)
def partners(request):
    '''
    Returns all partners for current fair
    '''
    fair = Fair.objects.get(current=True)
    partners = Partner.objects.filter(
        fair=fair
    ).order_by('-main_partner')
    data = [serializers.partner(request, partner) for partner in partners]
    return JsonResponse(data, safe=False)

@cache_page(60 * 5)
def organization(request):
    '''
    Returns all roles for current fair
    '''    
    all_groups = Group.objects \
        .prefetch_related('user_set__profile') \
        .order_by('name')

    # We only want groups that belong to roles that have been recruited during the current fair
    fair = Fair.objects.get(current=True)
    recruitment_period_roles = [period.recruitable_roles.all() for period in fair.recruitmentperiod_set.all()]
    role_groups = [role.group for roles in recruitment_period_roles for role in roles]
    groups = [group for group in all_groups if group in role_groups]

    data = [serializers.organization_group(request, group) for group in groups]
    return JsonResponse(data, safe=False)


def status(request):
    hostname = platform.node()
    python_version = platform.python_version()
    git_hash = subprocess.check_output('cd ~/git && git rev-parse HEAD', shell=True).decode("utf-8").strip()
    data = OrderedDict([
        ('status', "OK"),
        ('time', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        ('hostname', hostname),
        ('commit', git_hash),
        ('python_version', python_version),
    ])
    return JsonResponse(data, safe=False)

@cache_page(60 * 5)
def banquet_placement(request):
    '''

    Returns all banquet attendance for current fair. 
    The field job_title depends on weather a attendant is a user or exhibitor.
    '''

    fair = get_object_or_404(Fair, current = True)

    banquet_attendees = BanquetteAttendant.objects.filter(fair=fair)

    recruitment_applications = RecruitmentApplication.objects.filter(status='accepted')
    data = []
    for attendence in banquet_attendees:
        if attendence.user:
            recruitment_application = recruitment_applications.filter(user=attendence.user).first()
            if recruitment_application:
                attendence.job_title = 'Armada: ' + recruitment_application.delegated_role.name
            try:
                if not attendence.linkedin_url & attendence.user.profile.linkedin_url:
                    attendence.linkedin_url = attendence.user.profile.linkedin_url
            except:
                pass
        if attendence.exhibitor:
            job_title = attendence.job_title
            attendence.job_title = attendence.exhibitor.company.name
            if job_title:
                attendence.job_title += ': ' + job_title

        data.append(serializers.banquet_placement(request, attendence))
    return JsonResponse(data, safe=False)


@csrf_exempt
def student_profile(request):
    '''
    GET student profiles nickname by their id.
    Url: /student_profile?student_id={STUDENTPROFILEID}
    or
    PUT student profile nickname by the id
    URL: /api/student_profile?student_id={STUDENT_PROFILE_ID}
    DATA: json'{"nickname" : "{NICKNAME}"}'
    '''
    if request.method == 'GET':
        student_id = request.GET['student_id']
        student = get_object_or_404(StudentProfile, pk=student_id)
        data = OrderedDict([('nickname', student.nickname)])
    elif request.method == 'PUT':
        if request.body:
            student_id = request.GET['student_id']
            (student_profile, wasCreated) = StudentProfile.objects.get_or_create(pk=student_id)
            payload = json.loads(request.body.decode())
            if 'nickname' in payload:
                student_profile.nickname = payload['nickname']
                student_profile.save()
                data = OrderedDict([('nickname', student_profile.nickname)])
            else:
                return HttpResponse('No nickname in payload!', content_type='text/plain', status=406)
        else:
            return HttpResponse('No payload detected!', content_type='text/plain', status=406)
    else:
        return HttpResponseBadRequest('Unsupported method!', content_type='text/plain')

    return JsonResponse(data, safe=False)


def questions_GET(request):
    '''
    Handles a GET request to ais.armada.nu/api/questions
    Returns all questions and possible work fields, that belong to current survey.
    Each question can be of one of QuestionType types and have special fields depending on that type.
    Expected response:
    {
    "questions" : [
        {"id" : ID_0, "type" : "slider", "question" : "QUESTION_0", "min" : MIN, "max" : MAX, "logarithmic" : LOG, "units" : "UNITS"},
        {"id" : ID_1, "type" : "grading", "question" : "QUESTION_1", "count" : GRADING_COUNT},
        ...],
    "areas" : [
        {"id" : AREA_ID, "field" : "FIELD", "area" : "AREA"},
        ...]
    }
    Where:
        ID          - is an integer, identifying that specific question
        QUESTION    - is a string of that specific question
        MIN         - a float representing the lowest bound of the answer range
        MAX         - a float representing the highest bound of the answer range
        LOG         - a boolean value, selecting a logarithmic vs linear way of displaying the answer
        UNITS       - the name (plural) of units of entity in question
        AREA_ID     - is an integer, identifying that specific area
        FIELD       - the name of the field, which is a subcategory of AREA
        AREA        - the name of a field area, which is a supercategory of FIELD
    '''
    current_fair = get_object_or_404(Fair, current=True)
    survey = get_object_or_404(Survey, fair=current_fair)
    questions = QuestionBase.objects.filter(survey=survey)
    areas = WorkField.objects.filter(survey=survey)
    data = OrderedDict([
        ('questions', [serializers.question(question) for question in questions]),
        ('areas', [serializers.work_area(area) for area in areas])
    ])
    return JsonResponse(data, safe=False)


def questions_PUT(request):
    '''
    Handles a PUT request to ais.armada.nu/api/questions?id=STUDENT_ID
    Where STUDENT_ID is a unique uuid for a student.
    Expected payload looks like:
    {
    "questions" : [
        {"id" : ID, "answer" : ANSWER},
        ...]
    "areas" : [AREA_ID, ...]
    }
    Where:
        ID      - is an integer id for each question, that was sent with questions_GET
        ANSWER  - is either an int or a float, depending on the type of question
        AREA_ID - is an integer id for each area that was selected, that was sent with questions_PUT
    '''
    if request.body:
        student_id = request.GET['student_id']
        (student_profile, wasCreated) = StudentProfile.objects.get_or_create(pk=student_id)
        fair = get_object_or_404(Fair, current=true)
        survey = get_object_or_404(Survey, fair=fair)
        data = json.loads(request.body.decode())
        modified = False
        if 'questions' in data:
            modified = deserializers.answers(data['questions'], student)
        if 'areas' in data:
            areas = []
            for area in data['areas':
                if type(area) is int:
                    areas.add(area)
            if len(areas) > 0:
                deserializers.fields(areas, student, survey)
                modified = True
        if modified:
            return HttpResponse('Answers submitted!', content_type='text/plain')
        else:
            return HttpResponse('No answers were found in payload!', content_type='text/plain', status=406)
    else:
        return HttpResponse('No payload detected!', content_type='text/plain', status=406)


@csrf_exempt
def questions(request):
    '''
    ais.armada.nu/api/questions
    Handles GET request with questions_GET
    Handles PUT request with questions_PUT
    '''
    if request.methods == 'GET':
        return questions_GET(request)
    elif request.methods == 'PUT':
        return questions_PUT(request)
    else
        return HttpResponseBadRequest('Unsupported method!', content_type='text/plain')


def recruitment(request):
    '''
    ais.armada.nu/api/recruitment
    Returns all open recruitments and information about availeble roles for each recruitment.
    If there areno open recrutiment it returns an empty list.  
    '''
    fair = Fair.objects.get(current=True)
    recruitments = RecruitmentPeriod.objects.filter(fair=fair)
    recruitments = list(filter(lambda rec: (rec.start_date < timezone.now()) & (rec.end_date > timezone.now()), recruitments)) #Make sure only current recruitments are shown
    data = []
    for recruitment in recruitments:
        roles_info = []
        roles = recruitment.recruitable_roles.all()
        #Adds all roles available for this recruitment
        for role in roles:
            roles_info.append(OrderedDict([
                ('name', role.name),
                ('parent', role.parent_role.name),
                ('description', role.description),
                ]))
        data.append(OrderedDict([
            ('name', recruitment.name),
            ('start_date', recruitment.start_date),
            ('end_date', recruitment.end_date),
            ('roles', roles_info),
            ]))

    return JsonResponse(data, safe=False)
