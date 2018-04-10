# the first app for urls.py in the courts1 app

from django.conf.urls import url
from courts1 import views


urlpatterns = [
    url(r'^$', views.MainPageView.as_view()),
    url(r'^reserve/$', views.DisplayPageView.as_view()),
]
