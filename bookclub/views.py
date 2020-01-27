from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic.list import ListView

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/index.html', context)