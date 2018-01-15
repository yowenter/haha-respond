# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from functools import wraps
from collections import defaultdict
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, UserExam
import requests
from serializers import QuestionSerializer, ChoiceSerializer

from .models import Exam, Question, Vote, Choice
from haha_api.serializers import UserSerializer, ExamSerializer, VoteSerializer, QuestionSerializer

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "stram"))


# Create your views here.

def request_user_wrapper(func):
    @wraps(func)
    def inner(req):
        email = req.data.get('email') or req._request.environ.get('HTTP_X_EMAIL') or req.query_params.get('email')
        user = User.objects.filter(email=email).first()
        if not user:
            return Response("NO_EMAIL_PROVIDED_OR_NO_USER", status=status.HTTP_401_UNAUTHORIZED)

        req.data['user'] = UserSerializer(user).data
        req.data['user']['user_id'] = user.id
        return func(req)

    return inner


def ping(*args, **kwargs):
    return HttpResponse("pong")


class ExamApiView(APIView):
    def get(self, request, format=None):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VoteApiView(APIView):
    def post(self, request, format=None):
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


def publish_question(event, question_id, room_id):
    data = dict()
    data['event'] = event
    question = QuestionSerializer(Question.objects.filter(pk=question_id).first()).data
    choices = [ChoiceSerializer(c).data for c in Choice.objects.filter(question=question_id).all()]

    question['choices'] = choices
    data['data'] = question
    data['room'] = room_id
    try:
        r = requests.post('http://localhost:3100/event', json=data)
        r.raise_for_status()
    except Exception as e:
        raise e


class QuestionApiView(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = {}
        try:
            publish_question(request.data['event'], request.data['question_id'], request.data['question_id'])

            # data['event'] = request.data['event']
            # question = Question.objects.filter(pk=request.data['question_id'])
            # choices = Choice.objects.filter(question__id=request.data['question_id'])
            # question['choices'] = choices
            # data['data'] = question
            # data['room'] = request.data['exam_id']
            # r = requests.post('http://localhost:3100/event', json=data)
            # r.raise_for_status()
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        return Response(request.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        # data.pop("password")
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@request_user_wrapper
def join_room(request):
    from stream.haha_stream import encode_room_id

    room_id = request.data['room_id']
    user = request.data['user']

    exam = Exam.objects.filter(room_id=room_id).first()
    if not exam:
        return Response(dict(msg="room_id not found"), status=status.HTTP_400_BAD_REQUEST)

    if not UserExam.objects.filter(user_id=user['user_id'], exam_id=exam.exam_id).first():
        ue = UserExam(user_id=user['user_id'], exam_id=exam.exam_id)
        ue.save()

    room = encode_room_id(room_id)

    return Response(
        dict(room_id=room, exam=ExamSerializer(exam).data), status=status.HTTP_200_OK
    )


@api_view(['GET'])
@request_user_wrapper
def current_exam(request):
    room_id = request.data.get('room') or request.query_params.get('room')
    exam = Exam.objects.filter(room_id=room_id).first()
    if not exam:
        return Response(dict(msg="room_id not found"), status=status.HTTP_400_BAD_REQUEST)

    exam_data = ExamSerializer(exam).data

    question = QuestionSerializer(Question.objects.filter(pk=exam_data['current_question_id']).first()).data
    choices = [ChoiceSerializer(c).data for c in Choice.objects.filter(question=exam_data['current_question_id']).all()]

    question['choices'] = choices
    exam_data['question'] = question

    return Response(exam_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@request_user_wrapper
def vote(request):
    user = request.data['user']
    exam_id = request.data['exam_id']
    choice_id = request.data['choice_id']
    score = request.data['score']

    exam = Exam.objects.filter(exam_id=exam_id).first()
    if not exam:
        return Response(dict(msg="exam not found"), status=status.HTTP_400_BAD_REQUEST)

    choice = Choice.objects.filter(choice_id=choice_id).first()
    if not choice:
        return Response(dict(msg="choice not found"), status=status.HTTP_400_BAD_REQUEST)

    vote = Vote.objects.filter(exam_id=exam.exam_id, user_id=user['user_id'], choice_id=choice.choice_id).first()
    if vote:
        return Response(VoteSerializer(vote).data, status=status.HTTP_200_OK)

    vote = Vote(user_id=user['user_id'], exam_id=exam.exam_id, choice_id=choice.choice_id, score=int(score))
    vote.save()
    return Response(VoteSerializer(vote).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def report(request, exam_id):
    votes = Vote.objects.filter(exam_id=exam_id).all()
    users = set([v.user.email for v in votes])

    data = list()

    for u in users:
        total_score = sum([v.score for v in votes if v.user.email == u])
        right_question_count = len([v for v in votes if v.user.email == u and v.choice.is_right])
        data.append({
            "email": u,
            "total_score": total_score,
            "right_question_count": right_question_count
        })

    return Response(data, status=status.HTTP_200_OK)


def check_choice_right(choice_id, choices):
    return [c for c in choices if c.choice_id == choice_id and c.is_right]
