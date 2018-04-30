from django.shortcuts import render
from django.http import HttpResponse
from courts1.models import Loaded_Team
import themethod as tm
# Create your views here.
def testy(request):
    courtplayedon=tm.assigner()
    print(courtplayedon)
    if courtplayedon==0:
        istherecourts=False
    else:
        istherecourts=True
    return render(request, 'reserver/courtsdisplay.html',{'courtnum':courtplayedon ,'courts':istherecourts })
    
