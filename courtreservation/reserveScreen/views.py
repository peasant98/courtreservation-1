from django.shortcuts import render
from django.http import HttpResponse
from courts1.models import Loaded_Team
from reserveScreen.models import Court
import themethod as tm
import json
from courts1.views import finder
# Create your views here.
def testy(request):
    x = request.session['my_key']
    group_pk_used = int(x)
    print(group_pk_used)

    # you can do this method
    courter, my_assignedteam = tm.assigner(group_pk_used)

    if my_assignedteam != None:
        namer = str(my_assignedteam.team_name)
    else:
        namer = False
        #courter, my_assignedteam = tm.assigner(group_pk_used)

    courtnumber = int(my_assignedteam.court_id.courtNum)

    
    
    # need something here that tells what the group's team key is
    
    return render(request, 'reserver/courtsdisplay.html',{'teams':Loaded_Team.objects.all(), 'yo_team': namer, 'courtNum': courtnumber})
    
