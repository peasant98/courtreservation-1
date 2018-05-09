#Matthew Strong testing out views.py file 
#applying it with teams and players


#from django.shortcuts import render
# Create your views here.
# the views are taken from the urls.py - takes
# the requests and gives back a http response
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from courts1.models import Team, Player, Loaded_Team
from django.shortcuts import redirect
# is there are way to import other models from the other app??
#from courtreservation/courtsv1 import models
import random as rn

import courts1.method as mt

# you need the HttpResponse so far
# to be able to take in a request and then respond 
# with a httpresponse that tells the user what is going on 
def index(request):
    
    #need to connect to the database and get all of the teams
    all_teams = Team.objects.all()
    # this connects to the database, looks at the tables and finds all of the teams
    return render(request, 'courts1/index.html', {'all_teams': all_teams})

# create new views.() in this file for the results section that connects to what the user will eventually see after inputting the 
# amount of players that they want on a team, very important to ensure that there is database connections there as well!

def home(request):
    return render(request, 'courts1/home.html')
    

def finder(request):
    if request.method == 'POST':

        search_id = request.POST.get('testing', None)
        value = 0
        if search_id =='one':
            value = 1
        elif search_id == 'two':
            value = 2
        elif search_id == 'three':
            value = 3
        elif search_id == 'four':
            value = 4
        else:
            value = 5

        inqueue_team = mt.run_queue_analysis(value)
        
        # returns 0 or a team on 5 depending on what occurs within the actual algorithm 

        if inqueue_team == 0:
            return render(request, 'courts1/wait.html')
        else:
            all_loaded = Loaded_Team.objects.all()
            if len(all_loaded) % 2 == 0:
                # we have a full game here, and we want to return the members of the team as well
                first_team = all_loaded[len(all_loaded)-1]
                second_team = all_loaded[len(all_loaded)-2]
                first_players = first_team.player_set.all()
                second_players = second_team.player_set.all()
                return redirect('/reserver')
                #return render(request,'courts1/display_Courts.html', {'first_team': first_team, 'second_team': second_team, 'first_players': first_players, 'second_players': second_players})
            else:
                current_players = inqueue_team.player_set.all()
                return render(request, 'courts1/wait_for_another.html', {'inqueue_team': inqueue_team, 'current_players': current_players})
                

        return HttpResponse(value)
    else:
        return HttpResponse("Error! Error! Error!")
        
        
    