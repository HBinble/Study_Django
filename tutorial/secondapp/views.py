from django.shortcuts import render

from django.http import HttpResponse

def main(request) :
    return HttpResponse("<p>Secondapp Main 함수 호출</p>")
