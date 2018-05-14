from django.shortcuts import render
from django.http import HttpResponse
from courts1.models import Loaded_Team
from reserveScreen.models import Court
import themethod as tm
# Create your views here.
def testy(request):
    tm.assigner()
    return render(request, 'reserver/table.html',{'teams':Loaded_Team.objects.all()})
    
