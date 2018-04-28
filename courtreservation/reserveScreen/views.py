from django.shortcuts import render
from django.http import HttpResponse
from courts1.models import Loaded_Team
import themethod as tm
# Create your views here.
def testy(request):
    courtplayedon=tm.assigner()
    try:
        thecourtnum=courtplayedon.courtNum
        print(thecourtnum)
        return render(request, 'reserver/courtsdisplay.html',{'courtnum':thecourtnum})
    except:
        return HttpResponse("error")
