# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework import serializers, viewsets

from django.shortcuts import render, HttpResponse
from .models import User


# Create your views here.


def ping(*args, **kwargs):
    return HttpResponse("pong")
