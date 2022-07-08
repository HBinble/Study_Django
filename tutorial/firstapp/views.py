from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index1(request) :
    return HttpResponse("<u>Hello</u>")

def index2(request) :
    return HttpResponse("<p>index2 함수를 호출했습니다.</>")

def main(request) :
    return HttpResponse("<p>Main</p>")

def home(request) :
    return HttpResponse("<p>Home</p>")