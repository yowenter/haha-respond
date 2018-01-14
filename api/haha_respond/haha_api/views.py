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

from .models import Exam
from haha_api.serializers import UserSerializer


# Create your views here.


def ping(*args, **kwargs):
    return HttpResponse("pong")

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('exam_id', 'name')


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all().order_by('name')
    serializer_class = ExamSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
