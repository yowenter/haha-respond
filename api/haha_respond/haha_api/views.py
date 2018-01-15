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

from .models import Exam, Question, Vote
from haha_api.serializers import UserSerializer, ExamSerializer, VoteSerializer, QuestionSerializer


# Create your views here.


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


class QuestionApiView(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def publish_question(request):
    data = {}
    data['event'] = 'question_update'
    question = Question.objects.filter(pk=request.data['question_id'])
    data['data'] = question
    data['room'] = request.data['exam_id']
    try:
        r = requests.post('http://localhost:3100/event', json=data)
        r.raise_for_status()
    except Exception as e:
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)
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
def report(request):
    vs = Vote.objects.filter(exam=request.data)
    grouped_user_score = defaultdict(list)
    for v in vs:
        grouped_user_score[v.user].append(int(v.score))
    user_score_map = {k: sum(v) for k, v in grouped_user_score.iteritems()}
    result = sorted(user_score_map.iteritems(), key=lambda d: d[1], reverse=True)
    return Response(json.dumps(result))
