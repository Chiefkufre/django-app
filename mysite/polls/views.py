from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question
from django.template import loader


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pubDate')[:5]
    
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("You are looking at question %s. " % question_id)

def results(request, question_id):
    response = "you are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s. " % question_id)