from django.shortcuts import render
from django.views.generic import TemplateView
#comment for github testing
class MainPageView(TemplateView):
    def get(self, request, **kwargs):
    	return render(request, 'index.html', context=None)

class DisplayPageView(TemplateView):
    template_name = "courtsdisplay.html"


# Create your views here.
