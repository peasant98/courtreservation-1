# the first app for urls.py in the courts1 app

from django.conf.urls import url
from . import views

urlpatterns = [
    # if the user typed in /home, then
    # not typing anything after that would lead 
    # to this url, where views.bindex is called and
    # this leads us to the views.py file
    # matches with the courtsv1 app

    
    url(r'^$', views.home, name='home'),

    # courtsv1/<id of Team>
    url(r'^(?P<team_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^begin/', views.begin, name='begin'),
    url(r'^search/', views.search, name='begin'),
    url(r'^home/', views.home, name='home'),
    url(r'^finder/', views.finder, name='finder')
]
