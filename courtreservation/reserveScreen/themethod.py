from reserveScreen.models import Court
from courts1.models import Loaded_Team,Team,Player
import time

def assigner(grouper):
    print (str(grouper) + " is the value passed in.")
    for teamers in Loaded_Team.objects.all():
       teamers.refresh_from_db()
       teamers.save() 
    teams = list(Loaded_Team.objects.all())#team list#courts list of raw courts that havent been decided
    teams = [x for x in teams if x.isplaying==False]
    
    for courters in Court.objects.all():
       courters.refresh_from_db()
       courters.save()
    allcourts=list(Court.objects.all())
    courts=[x for x in allcourts if x.courtreserved==False]
    
    
    checker=0
    my_loaded_team = None
    
    if len(teams)==0 and len(Team.objects.all())==0 and len(courts)>0:
        matt_test_team = list(Loaded_Team.objects.all())
        my_teams = [x for x in matt_test_team if x.isplaying==True]
        done = False
        for z in my_teams:
            if done == True:
                break
            player_test = z.player_set.all()
            for i in player_test:
                
                if int(i.player_lt_value) == grouper:
                    my_loaded_team = z
                    done = True
        checker=1

    # extremely important while loop here!!!
    while len(teams)!=2 and checker==0 and len(courts)>-1 or (len(teams)==2 and len(courts)==0):
        
        time.sleep(2)
        if(len(courts)==0):
            print "fail, fail fail"
        checker=0
        print("The number of loaded teams is " + str(len(teams)))
        for teamers in Loaded_Team.objects.all():
            teamers.refresh_from_db()
            teamers.save()
        for courters in Court.objects.all():
            courters.refresh_from_db()
            courters.save()
        print "here"
        allcourts=list(Court.objects.all())
        courts=[x for x in allcourts if x.courtreserved==False]
        teams = list(Loaded_Team.objects.all())#team list#courts list of raw courts that havent been decided
        teams = [x for x in teams if x.isplaying==False]
        print "hero"
        # this is a big issue here
        if len(teams)==0 and len(Team.objects.all())>=0 and len(courts)>-1:
            matt_test_team = list(Loaded_Team.objects.all())
            my_teams = [x for x in matt_test_team if x.isplaying==True]
            done = False
            for z in my_teams:
                if done == True:
                    break
                player_test = z.player_set.all()
                for i in player_test:
                    
                    if int(i.player_lt_value) == grouper:
                        my_loaded_team = z
                        done = True
                        checker=1
            
        print "testing here"
        print(len(teams))
        print(len(courts))
        print(checker)
    print checker
    if ((len(teams)==2 and len(courts)>0)):# or (len(teams)==0 and len(courts)>0):\
        print "condition met"
        thecourt=courts[-1].courtNum

        for courts in Court.objects.all():
            if courts.courtNum==thecourt:
                courts.courtreserved=True
                actualcourt=courts
                courts.save()
        for team in Loaded_Team.objects.all():
            if team in teams:
                team.court_id=actualcourt
                # some changes here
                player_test = team.player_set.all()
                for i in player_test:
                    if int(i.player_lt_value) == grouper:
                        my_loaded_team = team
                        break
                team.isplaying=True
                team.save()
        #sfixreserved()
        return thecourt, my_loaded_team

    if (checker==1):
        
        return 0, my_loaded_team

    
    

