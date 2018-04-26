from django.shortcuts import render
from django.http import HttpResponse
from courts1.models import Loaded_Team
# Create your views here.

def testy(request):
    return HttpResponse('<h1>Testing Testing</h1>')