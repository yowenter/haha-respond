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


# todo


class ExamQuestionListInline(TabularInline):
    model = ExamQuestion


class ExamAdmin(admin.ModelAdmin):
    list_display = ['name', 'exam_id', 'state', 'pub_date', 'current_question_id']
    inlines = [ExamQuestionListInline]

    def save_model(self, request, obj, form, change):
        if change:
            if obj.current_question_id:
                publish_question('question_update', obj.current_question_id, obj.room_id)
            super(ExamAdmin, self).save_model(request, obj, form, change)

        else:
            super(ExamAdmin, self).save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Exam, ExamAdmin)
