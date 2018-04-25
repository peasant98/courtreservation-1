from __future__ import unicode_literals

from django.db import models
#from django.db.models import permalink
#from testing
#from testing.models import Court
# Create your models here.
# maybe need some model called full teams perhaps?
#from testing.models import Court

class Loaded_Team(models.Model):
    team_name = models.CharField(max_length=200)
    defense = models.CharField(max_length=250)
    offense = models.CharField(max_length=100)
    team_pic = models.CharField(max_length=1000)
    members = models.CharField(max_length=200, null=True)
    # this part here is very important for interfacting the two apps together in conjunction with each other. 
    
    # this next part here is critical for the court - team interaction in the back end!
    #court = models.ForeignKey('testing.Court', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.team_name + ' is the loaded team name!'

# this will serve as the loading dock for the teams that are waiting to be able to play a game
# for example, there could be a group of 5 that is waiting to be able to sent to a full game to play on the courts
# loaded teams will always have 5 people in them, this is very important
# players will belong to this new team of 5 with names and attack, defense, etc. 

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    defense = models.CharField(max_length=250)
    offense = models.CharField(max_length=100)
    team_pic = models.CharField(max_length=1000)
    members = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.team_name + ' and ' + self.offense
    # a unique key is created for each new object of class Team

class Player(models.Model):
    # when we create a player, it has to be linked to the team
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    loaded_team = models.ForeignKey(Loaded_Team, on_delete=models.CASCADE, null=True)
    file_type = models.CharField(max_length=10)
    player_name = models.CharField(max_length=200)
    # if you are adding or deleting attributes, then we have to do makemigrations
    # as well as everything else 
    # dealing with changes in the   database and migrate in general so that everything is synced up correctly
    def __str__(self):
        return self.player_name


