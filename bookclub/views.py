from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, CreateView, DeleteView
from .forms import AddBookForm, UpdateBookForm

class BookListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"
    paginate_by = 4
    ordering = ['-title']

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"

class BookCreateView(CreateView):
    model = Book
    template_name = "add_book.html"
    fields = ['title','author','genre','notes','year','image']

class BookUpdateView(UpdateView):
    model = Book
    template_name ="update_book.html"
    fields = ['title','author','genre','notes','year','image']
        