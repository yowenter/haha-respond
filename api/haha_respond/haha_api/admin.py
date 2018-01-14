# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.contrib import admin
from django.contrib.admin import TabularInline

# Register your models here.

from haha_api.models import Exam, Question, Choice, ExamQuestion


class ChoiceAdminInline(admin.TabularInline):
    model = Choice
    list_display = ['choice_text', 'question', 'is_right']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'question_text', 'difficulty']
    search_fields = ['question_text']
    inlines = [ChoiceAdminInline]


#


from .views import publish_question


class ExamQuestionListInline(TabularInline):
    model = ExamQuestion
    inline_actions = [publish_question]


class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_id', 'state', 'pub_date', ]
    inlines = [ExamQuestionListInline]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Exam, ExamAdmin)
# admin.site.register(ExamQuestion, ExamQuestionAdmin)
