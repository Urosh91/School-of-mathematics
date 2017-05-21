from django.core.exceptions import FieldError
from django.contrib import admin
from datetime import date

from . import models


class VideoInLine(admin.StackedInline):
    model = models.Video


class QuizInLine(admin.StackedInline):
    model = models.Quiz


class YearListFilter(admin.SimpleListFilter):
    title = 'year created'

    parameter_name = 'year'

    def lookups(self, request, model_admin):
        return (
            ('2015', '2015'),
            ('2016', '2016'),
            ('2017', '2017'),
        )

    def queryset(self, request, queryset):
        dates = ('2015', '2016', '2017')
        for date_1 in dates:
            if self.value() == date_1:
                return queryset.filter(created_at__gte=date(int(date_1), 1, 1),
                                       created_at__lte=date(int(date_1), 12, 31))


class CourseAdmin(admin.ModelAdmin):
    inlines = [VideoInLine, QuizInLine]
    search_fields = ['title', 'video__title']

    list_filter = [YearListFilter, 'created_at',]

    list_display = ['title', 'created_at']


class QuestionInLine(admin.StackedInline):
    model = models.Question


class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']
    inlines = [QuestionInLine,]


class AnswerInLine(admin.StackedInline):
    model = models.Answer


class QuestionAdmin(admin.ModelAdmin):
    try:
        fields = ['quiz', 'prompt', 'order', 'shuffle_answers']
    except FieldError:
        pass
    else:
        fields = ['quiz', 'prompt', 'order',]
    inlines = [AnswerInLine,]

    search_fields = ['prompt']

    list_display = ['prompt', 'quiz', 'order']

    list_editable = ['quiz', 'order']


class VideoAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'video_url']

admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.MultipleChoiceQuestion, QuestionAdmin)
admin.site.register(models.TrueFalseQuestion, QuestionAdmin)
admin.site.register(models.Answer)
