
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'), # 첫 argument의 url에 접속시, views 파일에 가서 home 함수의 내용을 실행하라.
]

