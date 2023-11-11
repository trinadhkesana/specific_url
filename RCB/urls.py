from RCB.views import *
from django.urls import path
app_name='c'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('abd/',abd,name='abd'),
]