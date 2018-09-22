from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    authors = Author.objects.all()
    return render(request, 'author/index.html', {'authors':authors})



def detail(request,author_id):
    author = Author.objects.get(id=author_id)
    return render(request,'author/detail.html',{'author':author})



