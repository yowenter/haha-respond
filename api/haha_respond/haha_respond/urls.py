"""haha_respond URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from haha_api import views
from rest_framework import serializers, viewsets, routers

router = routers.DefaultRouter()
# router.register('api/exams', views.ExamViewSet)

urlpatterns = [
    url(r'^api', include(router.urls)),
    url(r'^api/admin/', admin.site.urls),
    url(r'^api/ping', views.ping),
    url(r'^api/user', views.signup),
    url(r'^api/join', views.join_room),
    # url(r'^publish-question$', views.publish_question),
    url(r'^api/votes', views.VoteApiView.as_view()),
    url(r'^api/questions', views.QuestionApiView.as_view()),
    url(r'^api/exam/(.*)/report', views.report),
    url(r'^api/exams', views.ExamApiView.as_view()),
    url(r'^api/exam', views.current_exam)
]
