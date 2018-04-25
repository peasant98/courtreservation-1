from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def sendThem(request):
    return render(request, 'sendThem.html')