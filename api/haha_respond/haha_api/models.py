# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

import uuid


class Question(models.Model):
    question_id = models.CharField(max_length=64, primary_key=True, default=uuid.uuid4)
    question_text = models.TextField(max_length=255)
    difficulty = models.IntegerField()
    category = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_right = models.BooleanField()

    created_at = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return self.choice_text


class Exam(models.Model):
    exam_id = models.CharField(max_length=64, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=64)

    pub_date = models.DateTimeField()
    # state can be one of ["draft", "live", "closed"]
    state = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_created=True)


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam)
    question = models.ForeignKey(Question)

    created_at = models.DateTimeField(auto_created=True)


class Vote(models.Model):
    exam = models.ForeignKey(Exam)
    user = models.ForeignKey(User)
    choice = models.ForeignKey(Choice)
    question = models.ForeignKey(Question)

    created_at = models.DateTimeField(auto_created=True)
