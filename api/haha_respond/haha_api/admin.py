# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.contrib import admin
from django.contrib.admin import TabularInline
from django.contrib import messages

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

    readonly_fields = ('question_list',)

    def question_list(self, obj):
        from .models import ExamQuestion
        qs = ExamQuestion.objects.filter(exam_id=obj.exam_id).all()
        if qs:
            txt = "问题ID: 问题TEXT\n"
            txt += "\n".join(["%s :  %s" % (q.question_id, q.question.question_text) for q in qs])
            return txt

        return "没有可以激活的问题列表"

    def save_model(self, request, obj, form, change):
        error =None
        if change:
            if obj.current_question_id:
                try:
                    publish_question('question_update', obj.current_question_id, obj.room_id)
                except Exception as e:
                    error = e

            super(ExamAdmin, self).save_model(request, obj, form, change)
            if error:
                return messages.error(request, "保存成功。但发布推送消息失败，错误消息:%s" % str(error))

        else:
            super(ExamAdmin, self).save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Exam, ExamAdmin)
