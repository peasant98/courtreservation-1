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

def detail(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        #this will happen when we cannot find any team
        raise Http404("Team does not exist! You complete noob!")
    return render(request, 'courts1/detail.html', {'team': team})

def begin(request):
    return render(request, 'courts1/form.html')
#request is from hitting a submit button

def search(request):
    if request.method == 'POST':
        search_id = request.POST.get('first', None)
        #next_id = request.POST.get('second', None)
        value = int(search_id)



        '''if(value==1):
            allteams = Team.objects.all()
            firstnames = ['Bob', 'Matt', 'LeBron', 'Chris', 'Mike', 'Poopyhead', 'Cato', 'Alex', 'Baby', 'Jeff', 'Michael']
            lastnames = ['Sanders', 'Strong', 'James', 'Paul', 'Simmons', 'Poopypants', 'Gand', 'Height', 'Bobby', 'Lux', 'Jordan']
            firster = rn.randint(0,10)
            seconder = rn.randint(0,10)
            firstname = firstnames[firster]
            secondname = lastnames[seconder]

            first_title = ['Solo', 'The Lone', 'The Cool', 'Legendary', 'The Poopy', 'The Slow', 'The Gassy', 'The Speedy', 'Baby', 'Cute', 'Ugly']
            last_title = ['Boy', 'Baby', 'Shark', 'Devil', 'Baller', 'Disappointment', 'Legend', 'Toy', 'Jayhawk', 'Runner', 'Person Who Cannot Play Defense']
            first_int = rn.randint(0,10)
            seconder_int = rn.randint(0,10)
            first_teamname = first_title[first_int]
            second_name = last_title[seconder_int]
            full_teamname = first_teamname + ' ' + second_name

            full_name = firstname + ' ' + secondname
            one_player_team = Team.objects.create(team_name=full_teamname, defense='yep', offense='standard', team_pic='Solo team', members=1)
            first_player = Player.objects.create(team=one_player_team, file_type='.png', player_name=full_name)
            html = ("<h1> Player is here, it looks like! </h1>" + " and the player name is " + str(full_name))
            all_players = Player.objects.all()
            #return render(request, courtsv1/players.html, {'all_players': all_players, 'first_player': first_player})
        elif value>1 and value<6:
            first_title = ['Cool', 'Dumb', 'Fast', 'Legendary', 'Smelly', 'Happy', 'Farting', 'GOAT', 'Baby', 'Cute', 'Ugly']
            last_title = ['Boys', 'Babies', 'Sharks', 'Devils', 'Ballers', 'Disappointments', 'Legends', 'Toys', 'Jayhawks', 'Runners', 'People Who Cannot Play Defense']
            firster = rn.randint(0,10)
            seconder = rn.randint(0,10)
            firstname = first_title[firster]
            secondname = last_title[seconder]
            full_teamname = firstname + ' ' + secondname
            team1 = Team.objects.create(team_name=full_teamname, defense='yep', offense='standard', team_pic='Not worth taking a picture for', members=value)
            for i in range(0,value):
                firstnames = ['Bob', 'Matt', 'LeBron', 'Chris', 'Mike', 'Poopyhead', 'Cato', 'Alex', 'Baby', 'Jeff', 'Michael']
                lastnames = ['Sanders', 'Strong', 'James', 'Paul', 'Simmons', 'Poopypants', 'Gand', 'Height', 'Bobby', 'Lux', 'Jordan']
                fist = rn.randint(0,10)
                sec = rn.randint(0,10)
                firstname = firstnames[fist]
                secondname = lastnames[sec]
                full_name = firstname + ' ' + secondname
                team1.player_set.create(team=team1, file_type='.png', player_name=full_name)
            html = ("<h1> Team is here, it looks like! </h1>" + " and the team name is " + str(full_teamname))
            all_players = Player.objects.all()
        '''
        return render(request, 'courts1/results.html', {'all_players': all_players, 'team1': team1})

        # now for the most important aspect of the program, the code for handling when teams are here!
    
        

        # in the future, will need something like, return render(request, 'results.html')
        return HttpResponse('Hello World!')
        #return render(request, courtsv1/results.html,)
        # this is extremely important
    else:
        return render(request, 'courts1/form.html')

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
        
        
    