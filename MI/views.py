from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return render(request,'rohit.html')
def surya(request):
    return HttpResponse('<center><h1>Junior Mr 360</h1></center>')
