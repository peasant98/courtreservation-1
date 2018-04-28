from reserveScreen.models import Court
from courts1.models import Loaded_Team,Team,Player
teams = Loaded_Team.objects.all()#team list
courtQueue= list(Court.objects.all())#courts list of raw courts that havent been decided 
finalholder=[]
def assigner():
    for i in range(0,len(finalholder)):
        finalholder.pop()

    for courts in courtQueue:
        if(courts.courtreserved==True):#removing the reserved courts from the queue
            courtQueue.pop(courts)
            
    if len(courtQueue)<1 or (len(teams)!=2):
        print("There are no courts available!")# error message if there are no courts avaiable or somehow there are more than two teams
        return

    else:
        randCourt = courtQueue[len(courtQueue)-1]#setting randcourt to last thing in the queue of courtQueueerved courts
        courtQueue[len(courtQueue)-1].courtreserved=True
        finalholder.append(courtQueue[len(courtQueue)-1])

        for courts in Court.objects.all():
            if courts.courtNum==courtQueue[len(courtQueue)-1].courtNum:
                courts.courtreserved=True
                courts.save()


        courtQueue.pop()#removes the last item in the queue

        for team in teams:
            team.court_id=randCourt#setting the teams court to the last court in the queue of courts

        print("The teams have been assigned to play on "+ "Court"+str(randCourt.courtNum) + ".")
        if len(finalholder)>0:
            return finalholder[0]
            print(str(finalholder[0]))
    
    
    
    print("List of unreserved courts is this long:" + str(len(courtQueue)))
    for courts in courtQueue:
        print(str(courts))



