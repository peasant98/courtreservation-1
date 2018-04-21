# Algorithm created by Brian Nguyen
# Implementation done by Matthew Strong 

# brief notes for myself: make sure to create the new model of the teams in the queue already ready to play, from there, we can see if a game is going
# to be played based on the amount of teams in the loading dock for being able to go into a game!!
# because we want the algorithm to run once when a new player comes in, we can't necessarily form two teams from one player being entered in
# this change is VERY important, make sure to work on it after!!!

# Basketball Court Reservation Algorithm Version 2.0
###############################################################################################################

import random as rn
from courts1.models import Team, Player, Loaded_Team
# work on deleting multiple teams from a database when a group has multiple and different teams!!!!
class Team1:
	def __init__(self):
            self.players = []
            self.team_name = ""

        def create_team_name(self):
            self.team_name = "Tigers"

class Team2:
	def __init__(self):
            self.players = []
            self.team_name = ""

        def create_team_name(self):
            self.team_name = "Panthers"

class Group:
    def __init__(self):
            self.players = []
            self.numPlayers = 0

class Slayer:
    def __init__(self, player_name):
        self.name = player_name
# when team is formed, player is deleted.
def printQueue(inputQueue):
    print("Length is: " + str(len(inputQueue)))
    for i in range(len(inputQueue)):
        #print (inputQueue[i].numPlayers)
        #team_instance = inputQueue[i].player_set.all()

        print ("Group " + str(i+1)+ " has this many players: " + str(inputQueue[i].numPlayers))
# may have to adjust a lot of components of this.....
def run_queue_analysis(value):
    
    completedTeam1 = False
    completedTeam2 = False
    startingGame = False
    allteams = Team.objects.all()
    # returns a query set, so must put this as array in order to treat it as the queue that we want
    #teams_solo_array = [i for i in allteams]

    ##########################################################################################
    # anything that returns a queryset must be adjusted so that we are dealing with our "queue", which in this case will be 
    # an array!
    queueOfGroups = []
    for i in allteams:
        entry = Group()
        entry.players = ([x for x in i.player_set.all()])
        entry.numPlayers = (len([z for z in i.player_set.all()]))
        queueOfGroups.append(entry)


    # creating the initial queue that we will base everything from!!!!
    ##########################################################################################
    # for the full implementation, we will not necessarily need this - because this algorithm will run only once a player/team enters in their information
    #while startingGame == False: so far, this will not be necessary for the current testing
    print ("The length of the queue is " + str(len(queueOfGroups)))
    if len(queueOfGroups) >= 1:
        printQueue(queueOfGroups)

    name = ""
    T1 = Team1()
    T2 = Team2()
    
    #while startingGame == False:
    justFormedATeam = False
    totalNumPlayersPairedUp = 0

    #printQueue(queueOfGroups)  
    #print ("Enter the size of your group: ")
    #option = raw_input()
    #option = int(option)
    print ("The entered size of the group is: " + str(value))
    
    # taking user input for the amount of players that are being entered in 
    
    # for tomorrow: fix all of the 
    try:
        option = int(value)
        if option == 1:
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
            
            #original algorithm
            #print ("Enter your name")
            #newPlayerName = raw_input()
            #newPlayerName = str(newPlayerName)
            #new_player = Player(newPlayerName)
            newGroup = Group()
            newGroup.players.append(first_player)
            
            newGroup.numPlayers = 1
            totalNumPlayers = 0
            indicesOfGroupsPairing = [] 
            groupInQueueAdded = Group()
            #change is flag! - ask Brian about what flag does
            flag = 0

            for x in range(0, len(queueOfGroups)):
                
                if queueOfGroups[x].numPlayers + newGroup.numPlayers == 5 and flag != 2:
                    if len(indicesOfGroupsPairing) > 0:
                        if (len(indicesOfGroupsPairing) == 1):
                            indicesOfGroupsPairing = []
                            #for l in range(0, len(indicesOfGroupsPairing)):
                                #del(indicesOfGroupsPairing[l])
                        elif (len(indicesOfGroupsPairing) > 1):
                            indicesOfGroupsPairing = [indicesOfGroupsPairing[len(indicesOfGroupsPairing)-1]]
                            #for l in range(0, len(indicesOfGroupsPairing)-1):
                                #del(indicesOfGroupsPairing[l])
                    
                    totalNumPlayers = queueOfGroups[x].numPlayers
                    indicesOfGroupsPairing.append(x)
                    flag = 1
                
                if totalNumPlayers + queueOfGroups[x].numPlayers <= 5 and flag == 0:
                    totalNumPlayers = totalNumPlayers + queueOfGroups[x].numPlayers
                    indicesOfGroupsPairing.append(x)
                    if totalNumPlayers == 4:
                        flag = 2

            if totalNumPlayers + newGroup.numPlayers == 5:
                
                if completedTeam1 == False:
                    for k in range(0, len(indicesOfGroupsPairing)):
                        groupInQueueAdded = queueOfGroups[indicesOfGroupsPairing[k]]
                        for l in range(0, groupInQueueAdded.numPlayers):
                            T1.players.append(groupInQueueAdded.players[l])
                        queueOfGroups[indicesOfGroupsPairing[k]].numPlayers = 0          

                    T1.players.append(first_player)
                    
                    print("The players for Team 1 are:")
                    for m in range(0, len(T1.players)):
                        namedPlayer = str(T1.players[m].player_name)
                        print(namedPlayer)
                        
                    first_loaded_team = Loaded_Team.objects.create(team_name=full_teamname, defense='good', offense='noobs', team_pic='Fine players', members=5)
                    for i in T1.players:
                        first_loaded_team.player_set.create(loaded_team=first_loaded_team, file_type='.png', player_name=i.player_name)
                    #first_player.team.delete()
                    deletedAllPairedGroups = False
                    numGroupsDeleted = 0
                    #print(first_player.team.pk)
                    while (deletedAllPairedGroups == False):
                        
                        for n in range(0, len(queueOfGroups)):
                            print(first_player.team.pk)
                            if queueOfGroups[n].numPlayers == 0:
                                team_arr = []

                                for i in queueOfGroups[n].players:
                                    team_value = i.team.pk
                                    print team_value
                                    if team_value not in team_arr:
                                        team_arr.append(team_value)
                                for i in team_arr:
                                    print Team.objects.get(pk=i)
                                    Team.objects.get(pk=i).delete()
                                    print(first_player.team.pk)
                                del(queueOfGroups[n])
                                ###################
                                
                                numGroupsDeleted = numGroupsDeleted + 1                              
                                break
                        if numGroupsDeleted == len(indicesOfGroupsPairing):
                            one_player_team.delete()
                            deletedAllPairedGroups = True
                    
                    
                    print ("Created Team 1-D")
                    completedTeam1 = True
                    justFormedATeam = True
                    return first_loaded_team

                elif completedTeam2 == False and completedTeam1 == True:
                    for k in range(0, len(indicesOfGroupsPairing)):
                        groupInQueueAdded = queueOfGroups[indicesOfGroupsPairing[k]]
                        for l in range(0, groupInQueueAdded.numPlayers):
                            T2.players.append(groupInQueueAdded.players[l])
                        queueOfGroups[indicesOfGroupsPairing[k]].numPlayers = 0 

                    T2.players.append(first_player)

                    print("The players for Team 2 are:")
                    for m in range(0, len(T2.players)):
                        namedPlayer = str(T2.players[m].player_name)
                        print(namedPlayer)
                    
                    second_loaded_team = Loaded_Team.objects.create(team_name=full_teamname, defense='good', offense='noobs', team_pic='Fine players', members=5)
                    for i in T2.players:
                        second_loaded_team.player_set.create(loaded_team=second_loaded_team, file_type='.png', player_name=i.player_name)
                    deletedAllPairedGroups = False
                    numGroupsDeleted = 0
                    
                    while (deletedAllPairedGroups == False):
                        for n in range(0, len(queueOfGroups)):
                            if queueOfGroups[n].numPlayers == 0:
                                team_arr = []
                                for i in queueOfGroups[n].players:
                                    team_value = i.team.pk
                                    print team_value
                                    if team_value not in team_arr:
                                        team_arr.append(team_value)
                                for i in team_arr:
                                    print Team.objects.get(pk=i)
                                    Team.objects.get(pk=i).delete()
                                del(queueOfGroups[n])
                                ################################ fix this, this is critical to do 
                                
                                ###################
                                numGroupsDeleted = numGroupsDeleted + 1                             
                                break
                        if numGroupsDeleted == len(indicesOfGroupsPairing):
                            one_player_team.delete()
                            deletedAllPairedGroups = True

                    
                    print ("Created Team 2-D")
                    completedTeam2 = True
                    justFormedATeam = True
                    return second_loaded_team

            if justFormedATeam == False:
                queueOfGroups.append(newGroup)

            if completedTeam1 == True and completedTeam2 == True:
                startingGame = True
                print ("A game will start")
                if (len(queueOfGroups) > 0):
                    print ("These are the remaining groups")
                    printQueue(queueOfGroups)
                else:
                    print ("There are no remaining groups")
                #return T1, T2
        elif int(option) == 5:
            value = int(option)
            if completedTeam1 == False:
                
                first_title = ['Cool', 'Dumb', 'Fast', 'Legendary', 'Smelly', 'Happy', 'Farting', 'GOAT', 'Baby', 'Cute', 'Ugly']
                last_title = ['Boys', 'Babies', 'Sharks', 'Devils', 'Ballers', 'Disappointments', 'Legends', 'Toys', 'Jayhawks', 'Runners', 'People Who Cannot Play Defense']
                firster = rn.randint(0,10)
                seconder = rn.randint(0,10)
                firstname = first_title[firster]
                secondname = last_title[seconder]
                full_teamname = firstname + ' ' + secondname
                team1 = Team.objects.create(team_name=full_teamname, defense='yep', offense='standard', team_pic='Not worth taking a picture for', members=value)
                for i in range(0,5):
                    firstnames = ['Bob', 'Matt', 'LeBron', 'Chris', 'Mike', 'Poopyhead', 'Cato', 'Alex', 'Baby', 'Jeff', 'Michael']
                    lastnames = ['Sanders', 'Strong', 'James', 'Paul', 'Simmons', 'Poopypants', 'Gand', 'Height', 'Bobby', 'Lux', 'Jordan']
                    fist = rn.randint(0,10)
                    sec = rn.randint(0,10)
                    firstname = firstnames[fist]
                    secondname = lastnames[sec]
                    full_name = firstname + ' ' + secondname
                    added_player = team1.player_set.create(team=team1, file_type='.png', player_name=full_name)
                    T1.players.append(added_player)
                html = ("<h1> Team is here, it looks like! </h1>" + " and the team name is " + str(full_teamname))
                all_players = Player.objects.all()

                    #----------------------
                    #print ("Enter a name")
                    #newPlayerName = raw_input()
                    #newPlayerName = str(newPlayerName)
                    #new_player = Player(newPlayerName)
                    #-----------------------
                    #T1.players.append(new_player)                        
                
                print("The players for Team 1 are:")
                for m in range(0, len(T1.players)):
                    namedPlayer = str(T1.players[m].player_name)
                    print(namedPlayer)
                first_loaded_team = Loaded_Team.objects.create(team_name=full_teamname, defense='good', offense='noobs', team_pic='Fine players', members=5)
                for i in T1.players:
                    first_loaded_team.player_set.create(loaded_team=first_loaded_team, file_type='.png', player_name=i.player_name)
                    
                    # create new copy of player in loaded team maybe??
                T1.players[0].team.delete()    
                    


                
                print first_loaded_team.player_set.all()

                print ("Created Team 1-F")
                completedTeam1 = True
                justFormedATeam = True
                return first_loaded_team

            elif completedTeam2 == False and completedTeam1 == True:
                    
                first_title = ['Cool', 'Dumb', 'Fast', 'Legendary', 'Smelly', 'Happy', 'Farting', 'GOAT', 'Baby', 'Cute', 'Ugly']
                last_title = ['Boys', 'Babies', 'Sharks', 'Devils', 'Ballers', 'Disappointments', 'Legends', 'Toys', 'Jayhawks', 'Runners', 'People Who Cannot Play Defense']
                firster = rn.randint(0,10)
                seconder = rn.randint(0,10)
                firstname = first_title[firster]
                secondname = last_title[seconder]
                full_teamname = firstname + ' ' + secondname
                team1 = Team.objects.create(team_name=full_teamname, defense='yep', offense='standard', team_pic='Not worth taking a picture for', members=value)
                for i in range(0,5):
                    firstnames = ['Bob', 'Matt', 'LeBron', 'Chris', 'Mike', 'Poopyhead', 'Cato', 'Alex', 'Baby', 'Jeff', 'Michael']
                    lastnames = ['Sanders', 'Strong', 'James', 'Paul', 'Simmons', 'Poopypants', 'Gand', 'Height', 'Bobby', 'Lux', 'Jordan']
                    fist = rn.randint(0,10)
                    sec = rn.randint(0,10)
                    firstname = firstnames[fist]
                    secondname = lastnames[sec]
                    full_name = firstname + ' ' + secondname
                    added_player = team1.player_set.create(team=team1, file_type='.png', player_name=full_name)
                    T2.players.append(added_player)
                html = ("<h1> Team is here, it looks like! </h1>" + " and the team name is " + str(full_teamname))
                all_players = Player.objects.all()
                    
                    #print ("Enter a name")
                    #newPlayerName = raw_input()
                    #newPlayerName = str(newPlayerName)
                    #new_player = Player(newPlayerName)
                    #-------------------------------
                    #T2.players.append(new_player)                        
                
                print("The players for Team 2 are:")
                for m in range(0, len(T2.players)):
                    namedPlayer = str(T2.players[m].player_name)
                    print(namedPlayer)
                second_loaded_team = Loaded_Team.objects.create(team_name=full_teamname, defense='good', offense='noobs', team_pic='Fine players', members=5)
                for i in T1.players:
                    second_loaded_team.player_set.create(loaded_team=second_loaded_team, file_type='.png', player_name=i.player_name)
                    
                    # create new copy of player in loaded team maybe??
                T1.players[0].team.delete()  
                
                print("Created Team 2-F")
                completedTeam2 = True
                justFormedATeam = True 
                return second_loaded_team
            if completedTeam1 == True and completedTeam2 == True:
                startingGame = True
                print ("A game will start")
                if (len(queueOfGroups) > 0):
                    print ("These are the remaining groups")
                    printQueue(queueOfGroups)
                else:
                    print ("There are no remaining groups")
                #return T1, T2
        elif int(option) > 1 and int(option) < 6 and int(option) != 5:
            print("New Group!")
            newGroup = Group()
            # the new changes start here
            value = int(option)
            first_title = ['Cool', 'Dumb', 'Fast', 'Legendary', 'Smelly', 'Happy', 'Farting', 'GOAT', 'Baby', 'Cute', 'Ugly']
            last_title = ['Boys', 'Babies', 'Sharks', 'Devils', 'Ballers', 'Disappointments', 'Legends', 'Toys', 'Jayhawks', 'Runners', 'People Who Cannot Play Defense']
            firster = rn.randint(0,10)
            seconder = rn.randint(0,10)
            firstname = first_title[firster]
            secondname = last_title[seconder]
            full_teamname = firstname + ' ' + secondname
            team1 = Team.objects.create(team_name=full_teamname, defense='yep', offense='standard', team_pic='Not worth taking a picture for', members=value)
            for i in range(0,int(option)):
                firstnames = ['Bob', 'Matt', 'LeBron', 'Chris', 'Mike', 'Poopyhead', 'Cato', 'Alex', 'Baby', 'Jeff', 'Michael']
                lastnames = ['Sanders', 'Strong', 'James', 'Paul', 'Simmons', 'Poopypants', 'Gand', 'Height', 'Bobby', 'Lux', 'Jordan']
                fist = rn.randint(0,10)
                sec = rn.randint(0,10)
                firstname = firstnames[fist]
                secondname = lastnames[sec]
                full_name = firstname + ' ' + secondname
                added_player = team1.player_set.create(team=team1, file_type='.png', player_name=full_name)
                newGroup.players.append(added_player)
                newGroup.numPlayers = newGroup.numPlayers + 1
            html = ("<h1> Team is here, it looks like! </h1>" + " and the team name is " + str(full_teamname))
            all_players = Player.objects.all()
            print(team1)

            #or i in range(0, int(option)):
                #print ("Enter a name")
                #newPlayerName = raw_input()
                #newPlayerName = str(newPlayerName)
                #new_player = Player(newPlayerName)
                #newGroup.players.append(new_player)
                #newGroup.numPlayers = newGroup.numPlayers + 1

            totalNumPlayers = 0
            indicesOfGroupsPairing = [] 
            groupInQueueAdded = Group()
            flag = 0

            #this is case 1 where there's already two or more groups waiting and adding another group to them
            #would form a team
            #however, this also handles the case where the queue is like 4,2 and then if we add a group of 3
            #it will add the group of 3 to the group of 2
            print(len(queueOfGroups))
            for x in range(0, len(queueOfGroups)):
                print("test")
                print("Group " + str(x+1) + " num players: " + str(queueOfGroups[x].numPlayers))
                if queueOfGroups[x].numPlayers + newGroup.numPlayers == 5:
                    print(queueOfGroups[x].numPlayers)
                    indicesOfGroupsPairing = []
                    #for l in range(0, len(indicesOfGroupsPairing)):
                        #del(indicesOfGroupsPairing[l])
                    totalNumPlayers = queueOfGroups[x].numPlayers
                    indicesOfGroupsPairing.append(x)
                    flag = 1
                        
                if totalNumPlayers + queueOfGroups[x].numPlayers <= 5 and flag == 0:
                    totalNumPlayers = totalNumPlayers + queueOfGroups[x].numPlayers
                    indicesOfGroupsPairing.append(x)
                print("The total num players is " + str(totalNumPlayers))

            #print("The index of the group with the total number of players is " + str(indicesOfGroupsPairing[0]))
            #print("The total number of players is " + str(totalNumPlayers))

                if totalNumPlayers + newGroup.numPlayers == 5:
                    if completedTeam1 == False:
                        for k in range(0, len(indicesOfGroupsPairing)):
                            groupInQueueAdded = queueOfGroups[indicesOfGroupsPairing[k]]
                            for l in range(0, groupInQueueAdded.numPlayers):
                                T1.players.append(groupInQueueAdded.players[l])
                            #here I tagged the used groups by making their numPlayers equal to 0
                            queueOfGroups[indicesOfGroupsPairing[k]].numPlayers = 0    
                        for l in range (0, newGroup.numPlayers):
                            T1.players.append(newGroup.players[l] )

                        print("The players for Team 1 are:")
                        for m in range(0, len(T1.players)):
                            namedPlayer = str(T1.players[m].player_name)
                            print(namedPlayer)


                        first_loaded_team = Loaded_Team.objects.create(team_name=full_teamname, defense='good', offense='noobs', team_pic='Fine players', members=5)
                        for i in T1.players:
                            first_loaded_team.player_set.create(loaded_team=first_loaded_team, file_type='.png', player_name=i.player_name)
                    
                        # create new copy of player in loaded team maybe??
                        #T1.players[0].team.delete()  
                        # don't think we need this??
                        deletedAllPairedGroups = False
                        numGroupsDeleted = 0

                        while (deletedAllPairedGroups == False):
                            for n in range(0, len(queueOfGroups)):
                    
                                if queueOfGroups[n].numPlayers == 0:
                                    ############################ kanban major changes here, make sure to look over
                                    team_arr = []
                                    for i in queueOfGroups[n].players:
                                        team_value = i.team.pk
                                        print team_value
                                        if team_value not in team_arr:
                                            team_arr.append(team_value)
                                    for i in team_arr:
                                        print Team.objects.get(pk=i)
                                        Team.objects.get(pk=i).delete()
                                    # maybe we will need this I don't know yet....
                                    #queueOfGroups[n].players[0].team.delete()
                                    del(queueOfGroups[n])
                                    
                                    numGroupsDeleted = numGroupsDeleted + 1                             
                                    break
                            if numGroupsDeleted == len(indicesOfGroupsPairing):
                                team1.delete()
                                deletedAllPairedGroups = True    
                                
                        print ("Created Team 1-E")
                        completedTeam1 = True
                        justFormedATeam = True 
                        return first_loaded_team

                    elif completedTeam2 == False and completedTeam1 == True:
                        for k in range(0, len(indicesOfGroupsPairing)):
                            groupInQueueAdded = queueOfGroups[indicesOfGroupsPairing[k]]
                            for l in range(0, groupInQueueAdded.numPlayers):
                                T2.players.append(groupInQueueAdded.players[l])                            
                                    #here I tagged the used groups by making their numPlayers equal to 0
                            queueOfGroups[indicesOfGroupsPairing[k]].numPlayers = 0    
                                
                        for l in range (0, newGroup.numPlayers):
                            T2.players.append(newGroup.players[l])    
                                
                        print("The players for Team 2 are:")
                        for m in range(0, len(T2.players)):
                            namedPlayer = str(T2.players[m].player_name)
                            print(namedPlayer)

                        second_loaded_team = Loaded_Team.objects.create(team_name=full_teamname, defense='good', offense='noobs', team_pic='Fine players', members=5)
                        for i in T2.players:
                            second_loaded_team.player_set.create(loaded_team=second_loaded_team, file_type='.png', player_name=i.player_name)

                        deletedAllPairedGroups = False
                        numGroupsDeleted = 0

                        while (deletedAllPairedGroups == False):
                            for n in range(0, len(queueOfGroups)):
                                if queueOfGroups[n].numPlayers == 0:
                                    team_arr = []
                                    for i in queueOfGroups[n].players:
                                        team_value = i.team.pk
                                        print team_value
                                        if team_value not in team_arr:
                                            team_arr.append(team_value)
                                    for i in team_arr:
                                        print Team.objects.get(pk=i)
                                        Team.objects.get(pk=i).delete()
                                    del(queueOfGroups[n])
                                    
                                    ###################
                                    numGroupsDeleted = numGroupsDeleted + 1                                                                      
                                    break
                            if numGroupsDeleted == len(indicesOfGroupsPairing):
                                team1.delete()
                                deletedAllPairedGroups = True    
                        print ("Created Team 2-E")
                        
                        completedTeam2 = True
                        justFormedATeam = True 
                        return second_loaded_team
        
            #this is case 2 where there's already one group waiting and adding another group 
            #to them would form a team
                
            else:
                for i in range(0,len(queueOfGroups)):
                    if queueOfGroups[i].numPlayers + newGroup.numPlayers == 5 and completedTeam1 == False:
                        for x in range (0, queueOfGroups[i].numPlayers):
                            T1.players.append(queueOfGroups[i].players[x])
                        for y in range (0, newGroup.numPlayers):
                            T1.players.append(newGroup.players[y])

                        first_loaded_team = Loaded_Team.objects.create(team_name=full_teamname, defense='good', offense='noobs', team_pic='Fine players', members=5)
                        for i in T1.players:
                            first_loaded_team.player_set.create(loaded_team=first_loaded_team, file_type='.png', player_name=i.player_name)
                        team_arr = []
                        for c in queueOfGroups[i].players:
                            team_value = c.team.pk
                            if team_value not in team_arr:
                                team_arr.append(team_value)
                        for c in team_arr:
                            print Team.objects.get(pk=c)
                            Team.objects.get(pk=c).delete()



                        del(queueOfGroups[i])
                        team1.delete()
                        
                        print ("Created Team 1-B")
                        completedTeam1 = True
                        justFormedATeam = True
                        return first_loaded_team

                    elif queueOfGroups[i].numPlayers + newGroup.numPlayers == 5 and completedTeam2 == False:
                        for x in range (0, queueOfGroups[i].numPlayers):
                            T2.players.append(queueOfGroups[i].players[x])
                        for y in range (0, newGroup.numPlayers):
                            T2.players.append(newGroup.players[y])
                        team_arr = []
                        second_loaded_team = Loaded_Team.objects.create(team_name=full_teamname, defense='good', offense='noobs', team_pic='Fine players', members=5)
                        for i in T2.players:
                            second_loaded_team.player_set.create(loaded_team=second_loaded_team, file_type='.png', player_name=i.player_name)
                        for c in queueOfGroups[i].players:
                            team_value = c.team
                            print team_value
                            if team_value not in team_arr:
                                team_arr.append(team_value)
                        for c in team_arr:
                            print Team.objects.get(pk=c)
                            Team.objects.get(pk=c).delete()
                            
                        del(queueOfGroups[i])
                        team1.delete()
                        ###################
                        # deleting from the database
                        ###################################
                        print ("Created Team 2-B")
                        completedTeam2 = True
                        justFormedATeam = True
                        return second_loaded_team
                
            if justFormedATeam == False:
                queueOfGroups.append(newGroup)
            
            if completedTeam1 == True and completedTeam2 == True:
                startingGame = True
                print ("A game will start")
                if (len(queueOfGroups) > 0):
                    print ("These are the remaining groups")
                    printQueue(queueOfGroups)
                    
                else:
                    print ("There are no remaining groups")
                return T1, T2
        else:
            print "Invalid amount of players!"
            print "Nothing will entered into the database, you noob!!!!"
        return 0
    # I don't think that we will need this!!!
    except ValueError:
        print "Please enter in a valid option!"
        print ""

    # some kind of first team needs to be returned!!!
    
    
if __name__ == "__main__":
    value = 5
    lteam = run_queue_analysis(value)
