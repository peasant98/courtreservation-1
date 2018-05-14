from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from reserveScreen.models import Court
from courts1.models import Loaded_Team,Team,Player
# Create your views here.
def sendThem(request):
    return render(request, 'sendThem.html')
def nuke(request):
    Loaded_Team.objects.all().delete()
    Team.objects.all().delete()
    Player.objects.all().delete()

    for courts in Court.objects.all():
        courts.courtreserved=False
        courts.save()
    
    return HttpResponse('Boom')