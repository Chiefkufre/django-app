from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    
    return HttpResponse("Hello, welcome to my first django application")

def login(request):
    return JsonResponse({
        "msg": "return back jsonify response"
    })