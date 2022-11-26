from django.shortcuts import render
from django.http import HttpResponse


#http://localhost:8000/polls/

# Create your views here.
def index(request):
    return HttpResponse("hi pup")

