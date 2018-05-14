from reserveScreen.models import Court
from courts1.models import Loaded_Team,Team,Player
import time

def assigner():
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
    
    if len(teams)==0 and len(Team.objects.all())==0 and len(courts)>0:
        checker=1
    
    while len(teams)!=2 and checker==0 and len(courts)>0:
        time.sleep(10)
        print("The number of loaded teams is " + str(len(teams)))
        for teamers in Loaded_Team.objects.all():
            teamers.refresh_from_db()
            teamers.save()
        for courters in Court.objects.all():
            courters.refresh_from_db()
            courters.save()
        allcourts=list(Court.objects.all())
        courts=[x for x in allcourts if x.courtreserved==False]
        teams = list(Loaded_Team.objects.all())#team list#courts list of raw courts that havent been decided
        teams = [x for x in teams if x.isplaying==False]
        assigner()
    
    if (len(teams)==2 and len(courts)>0):# or (len(teams)==0 and len(courts)>0):
        thecourt=courts[-1].courtNum
        for courts in Court.objects.all():
            if courts.courtNum==thecourt:
                courts.courtreserved=True
                actualcourt=courts
                courts.save()
        for team in Loaded_Team.objects.all():
            if team in teams:
                team.court_id=actualcourt
                team.isplaying=True
                team.save()
        #sfixreserved()
        return thecourt
    

