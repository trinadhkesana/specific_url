from CSK.views import *
from django.urls import path
app_name='a'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('raina/',raina,name='raina'),
]