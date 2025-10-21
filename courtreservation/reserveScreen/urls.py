from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^reservation/$', views.reservation_grid, name='reservation_grid'),
    url(r'^api/reserve/$', views.make_reservation, name='make_reservation'),
    url(r'^', views.testy, name='testy'),

]