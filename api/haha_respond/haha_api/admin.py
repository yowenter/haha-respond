# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from haha_api.models import Exam, Question, Choice, ExamQuestion


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'question_text', 'difficulty']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'question', 'is_right']


class ExamAdmin(admin.ModelAdmin):
    list_display = ['exam_id', 'state', 'pub_date']


class ExamQuestionAdmin(admin.ModelAdmin):
    list_display = ['exam_id', 'question']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamQuestion, ExamQuestionAdmin)


