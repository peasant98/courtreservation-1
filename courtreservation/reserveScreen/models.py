from django.db import models

# Create your models here.

'''
This is just a test I really need to think about how to have one of the fields in the Court class be a field of Team Objects from the first app
but for testing purposes this is what I will be testing with right now
'''
class Court(models.Model):
    courtNum=models.IntegerField(default=0)
    courtreserved= models.BooleanField(default=False)
    '''
    team1=models.manytomany(Team)
    team2=models.manytomany(Team)

    what is the advantage of this over foreign key?
    '''

    #team1=models.ForeignKey(Team,on_delete=models.CASCADE)#, related_name='team1')
    #team2=models.ForeignKey(Team,on_delete=models.CASCADE, related_name='team2')
    def __str__(self):
        return 'Court'+str(self.courtNum)

class Teamers(models.Model):
    p1=models.CharField(max_length=250)
    p2=models.CharField(max_length=250)
    p3=models.CharField(max_length=250)
    p4=models.CharField(max_length=250)
    p5=models.CharField(max_length=250)

    court=models.ForeignKey(Court,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.p1






