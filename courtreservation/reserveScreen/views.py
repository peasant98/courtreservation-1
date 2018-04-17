from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testy(request):
    return HttpResponse('<h1>Testing Testing</h1>')