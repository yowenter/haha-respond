# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.db import models

from django.contrib.auth.models import User

import uuid


class Question(models.Model):
    question_id = models.CharField(max_length=64, primary_key=True, default=uuid.uuid4)
    question_text = models.TextField(max_length=255)
    difficulty = models.IntegerField()
    category = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    choice_id = models.CharField(max_length=64, primary_key=True, default=uuid.uuid4)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_right = models.BooleanField()

    created_at = models.DateTimeField(auto_created=True, auto_now=True)

    def __unicode__(self):
        return self.choice_text


def _generate_random_room():
    return "".join([str(random.randint(0, 9)) for i in range(4)])


class Exam(models.Model):
    exam_id = models.CharField(max_length=64, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=64)
    room_id = models.CharField(max_length=64, default=_generate_random_room, db_index=True)
    current_question_id = models.CharField(max_length=64, blank=True)
    last_question_id = models.CharField(max_length=64, blank=True)


    pub_date = models.DateTimeField()
    # state can be one of ["draft", "live", "closed"]
    state = models.CharField(max_length=64, default="draft")

    created_at = models.DateTimeField(auto_created=True, auto_now=True)


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam)
    question = models.ForeignKey(Question)

    created_at = models.DateTimeField(auto_created=True, auto_now=True)


class Vote(models.Model):
    vote_id = models.CharField(max_length=64, primary_key=True, default=uuid.uuid4)
    exam = models.ForeignKey(Exam, null=True)
    choice = models.ForeignKey(Choice, null=True)
    user = models.ForeignKey(User, null=True)
    score = models.IntegerField()

    created_at = models.DateTimeField(auto_created=True, auto_now=True)


class UserExam(models.Model):
    uuid = models.CharField(max_length=64, primary_key=True, default=uuid.uuid4)
    exam = models.ForeignKey(Exam)
    user = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_created=True, auto_now=True)
