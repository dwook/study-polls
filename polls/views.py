from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("설문조사 어플리케이션")

def detail(request, question_id):
    return HttpResponse("설문조사 %s 상세페이지" % question_id)

def results(request, question_id):
    response = "설문조사 %s 결과"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("설문조사 %s 투표중" % question_id)
