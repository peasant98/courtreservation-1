from django.http import HttpResponse
from django.shortcuts import render
from courts1.models import Team, Player, Loaded_Team
from django.shortcuts import redirect
import time

def makeThemWait(contextual):
    allteams=Loaded_Team.objects.all()
    if len(allteams)==0 and contextual!=1:
        return
    while(len(allteams)<2 and len(allteams)!=0):
        allteams=Loaded_Team.objects.all()
        print("the length of the loaded teams is " + str(len(allteams)))
        time.sleep(1)
        makeThemWait(0)