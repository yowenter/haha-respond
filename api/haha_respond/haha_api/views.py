# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from collections import defaultdict
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
import requests
from serializers import QuestionSerializer, ChoiceSerializer

from .models import Exam, Question, Vote, Choice
from haha_api.serializers import UserSerializer, ExamSerializer, VoteSerializer, QuestionSerializer


# Create your views here.

def request_user_wrapper(*args):
    pass


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
def join_room(request):
    return Response(
        dict(room_id="1234"), status=status.HTTP_200_OK
    )


@api_view(['GET'])
def current_exam(request):
    return Response({
        "room_id": "1234",
        "state": "live",
        "question": {
            "question_id": "1234",
            "question_text": "生命宇宙及一切的答案是什么？",
            "category": "Life",
            "difficulty": 1,
            "choices": [
                {
                    "choice_id": "1234",
                    "choice_text": "42",
                    "is_right": True
                },
                {
                    "choice_id": "1234",
                    "choice_text": "41",
                    "is_right": False
                },
                {
                    "choice_id": "1234",
                    "choice_text": "24",
                    "is_right": False
                }
            ]
        }
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def report(request):
    vs = Vote.objects.filter(exam_id=request.data)
    cs = Choice.objects.all()
    grouped_user_score = defaultdict(list)
    grouped_user_question = defaultdict(list)

    for v in vs:
        grouped_user_score[v.email].append(int(v.score))
        grouped_user_question[v.email].append(v.choice_id)

    user_score_map = {k: sum(v) for k, v in grouped_user_score.iteritems()}

    user_question_map = {}
    for u in grouped_user_question:
        user_question_map[u] = 0
    for email, choices in grouped_user_question:
        for c in choices:
            if check_choice_right(c, cs):
                user_question_map[email] += 1

    result = []
    for k in user_score_map:
        r = {}
        r['email'] = k
        r['total_score'] = user_score_map[k]
        r['right_question_count'] = user_question_map[k]
        result.append(r)

    return Response(json.dumps(result))


def check_choice_right(choice_id, choices):
    return [c for c in choices if c.choice_id == choice_id and c.is_right]
