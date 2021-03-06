import csv
from django.contrib import messages
from django.contrib import admin
from .models import Event, EventAttendence, EventQuestion, EventAnswer
from django.http import HttpResponse
from lib.util import image_preview


def mark_accepted(modeladmin, request, queryset):
    queryset.update(status='A')


def mark_declined(modeladmin, request, queryset):
    queryset.update(status='D')


def mark_submitted(modeladmin, request, queryset):
    queryset.update(status='S')


def mark_canceled(modeladmin, request, queryset):
    queryset.update(status='C')


# Exports all the EventAnswers that belong to a single Event
# (Could be expanded to include User information)
def export_as_csv(modeladmin, request, queryset):
    if len(queryset) != 1:
        modeladmin.message_user(request,
                                "Please select a single event to export", level=messages.ERROR)
        return

    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename=event.csv'

    # We have already checked that it is a single event
    event_id = queryset.first().id
    csv_headers = ['First name (user)', 'Last name (user)', 'Email (user)']
    csv_headers.append('Status')
    question_list = []
    for question in EventQuestion.objects.filter(event__id=event_id):
        question_list.append(question.id)
        csv_headers.append(question.question_text)

    writer = csv.writer(response, quoting=csv.QUOTE_ALL)
    writer.writerow(csv_headers)
    for attendence in EventAttendence.objects.filter(event__id=event_id):
        user = attendence.user
        if user is None:
            user_information = [None, None, None]
        else:
            user_information = [
                attendence.user.first_name,
                attendence.user.last_name,
                attendence.user.email,
            ]

        status = [attendence.status]

        answers = []
        for question in question_list:
            event_answer = (EventAnswer.objects
                            .filter(question__id=question)
                            .filter(attendence__id=attendence.id)
                            .first())
            if event_answer is not None:
                answers.append(event_answer.answer)
            else:
                answers.append(None)
        writer.writerow(user_information + status + answers)
    return response


class QuestionInline(admin.StackedInline):
    model = EventQuestion
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
            'fair', 'extra_field', 'name', 'event_start', 'event_end', 'capacity', 'description', 'description_short',
            'location', 'attendence_description', 'attendence_approvement_required', 'published',)
        }),
        ('Registration Details', {
            'classes': ('collapse',),
            'fields': ('external_signup_url', 'registration_required', 'registration_start', 'registration_end',
                       'registration_last_day_cancel', 'allowed_groups',)
        }),
        ('Email', {
            'classes': ('collapse',),
            'fields': (
            'send_submission_mail', 'submission_mail_subject', 'submission_mail_body', 'confirmation_mail_subject',
            'confirmation_mail_body', 'rejection_mail_subject', 'rejection_mail_body')
        }),
        ('Images', {
            'classes': ('collapse',),
            'fields': ('image_original', 'event_image_preview',)
        }),
        (None, {
            'fields': ('tags',)
        })
    )
    search_fields = ('name',)
    # order by fair in first hand
    ordering = ('fair', 'name',)
    list_filter = ('published', 'registration_required', 'fair',)
    readonly_fields = ('event_image_preview', 'extra_field',)
    inlines = [QuestionInline]
    filter_horizontal = ("allowed_groups",)
    actions = [export_as_csv]

    event_image_preview = image_preview('image')


class AnswerInline(admin.StackedInline):
    model = EventAnswer


class EventAttendenceAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('id', 'first_name', 'last_name', 'event', 'status',)

    def first_name(self, obj):
        if obj.user:
            return obj.user.first_name
        return "External"

    def last_name(self, obj):
        if obj.user:
            return obj.user.last_name
        return "User"

    search_fields = ['id', 'user__first_name', 'user__last_name',
                     'event__name']
    list_filter = ('status', 'event')
    actions = [mark_accepted, mark_declined, mark_submitted,
               mark_canceled]


admin.site.register(EventAttendence, EventAttendenceAdmin)
