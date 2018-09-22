from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    return render(request,'book/index.html')

def list(request):
    books = Book.objects.all()
    return render(request, 'book/list.html', {'books':books})

def detail(request, bookid):

    book = Book.objects.get(id=bookid)
    return render(request, 'book/detail.html', {'book':book})