# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
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


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all().order_by('name')
    serializer_class = ExamSerializer


class VoteApiView(APIView):
    def get(self, request, format=None):
        vs = Vote.objects.all()
        serializer = VoteSerializer(vs, many=True)
        return Response(serializer.data)

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
        data.pop("password")
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
