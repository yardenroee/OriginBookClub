from django.shortcuts import render, redirect
from .models import Book
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"
    paginate_by = 4
    ordering = ['-title']

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    def post(self, *args, **kwargs):
        if self.request.method == "POST":
            book = Book.objects.get(pk=self.kwargs.get('pk'))
            user = self.request.user
            user.profile.favorites.add(book)
            user.save()
        return redirect('index')

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "add_book.html"
    fields = ['title','author','genre','about','year','image']

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name ="update_book.html"
    fields = ['title','author','genre','about','year','image']

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = "/" #will redirect to home page on successful deletion