# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render, HttpResponse
from .models import User
from .models import Exam


# Create your views here.


def ping(*args, **kwargs):
    return HttpResponse("pong")

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('exam_id', 'name')


class ExamApi(APIView):
    def get(self, request, format=None):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer)
