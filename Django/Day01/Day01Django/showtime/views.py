from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.

def freshen(request):
    c = datetime.datetime.now()
    return HttpResponse(c)

def index1(request):
    c = datetime.datetime.now()
    return render(request, 'index1.html',{'time':c})
