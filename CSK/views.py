from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return render(request,'dhoni.html')
def raina(request):
    return HttpResponse('<center><h1>Mr IPL</h1></center>')
