from django.shortcuts import render

from django.http import HttpResponse

def index1(request) :
    return HttpResponse("<p>안녕하세요~ 오늘은 비가 옵니다.</p>")

def index6(request) :
    return HttpResponse("<p>내일은 맑음입니다.</p>")

def index2(request) :
    return HttpResponse("<p>오늘 온도는 28도 입니다.</p>")