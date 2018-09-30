from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    usertype = UserType.objects.get(id=1)
    return render(request, 'index.html', {'usertype': usertype})

