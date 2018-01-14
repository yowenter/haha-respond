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


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
