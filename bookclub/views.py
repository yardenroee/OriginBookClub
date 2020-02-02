from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Book, UserBookNotes
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from .forms import AddUpdateBookForm, BookNoteUpdateForm

class BookListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"
    paginate_by = 4
    ordering = ['-title']
    
class SearchListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "books"
    paginate_by = 4
    ordering = ['-title']
    
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        qs = Book.objects.all()
        if query is not None:
            qs = qs.filter(
                Q(title__icontains = query) |
                Q(author__icontains = query) |
                Q(year__icontains = query))
        return qs
    def get_context_data(self, *args, **kwargs):
        context= super(SearchListView, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "book_detail.html"
    def post(self, *args, **kwargs):
        user = self.request.user
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        if self.request.method == "POST":
            if user.is_authenticated:
                if book not in user.profile.favorites.all():
                    user.profile.favorites.add(book)
                    user.save()
                    return redirect('favorites')
                else:
                    user.profile.favorites.remove(book)
                    user.save()
                    return redirect('favorites')
            else:
                return redirect('login')
        return redirect('favorites')

    def get_context_data(self, **kwargs):
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        user = self.request.user
        if user.is_authenticated:
            book_notes = UserBookNotes.objects.filter(book=book, user=user) 
            if book_notes and user.id == book_notes.values()[0].get('user_id'):
                print(book_notes.values()[0].get('text'))
                context = super().get_context_data(**kwargs)
                context['favorites'] = self.request.user.profile.favorites.all()
                context['book_notes'] = book_notes.values()[0].get('text')
            else:
                print('here in ELSE gcd of detailview')
                context = super().get_context_data(**kwargs)
                context['book_notes'] = ""
        return context

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "add_book.html"
    fields = ['title','author','genre','about','year','image']


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "update_book.html"
    UserBookNotesFormSet = BookNoteUpdateForm
    fields = ['title','author','genre','about','year','image']
    def post(self, *args, **kwargs):
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        user = self.request.user
        book_notes = UserBookNotes.objects.filter(book=book, user=user)
        print(book_notes)
        if self.request.method == "POST":
            if book_notes: #if notes on book 
                print('book notes exists')
                form1 = self.UserBookNotesFormSet(self.request.POST)
                if form1.is_valid():
                    print('2')
                    book_notes.update(text = form1.cleaned_data.get('text'))
            else:#if no book notes
                print('no book notes')
                form1 = self.UserBookNotesFormSet()
                text = self.request.POST.get('text') # get the text field before submitting
                new_note = UserBookNotes.objects.create(book = book, user = user, text = text)
                new_note.save()
        return redirect('/')
    
    def get_context_data(self, **kwargs):
        book = Book.objects.get(pk=self.kwargs.get('pk'))
        user = self.request.user
        context = super().get_context_data(**kwargs)
        book_notes = UserBookNotes.objects.filter(book=book, user=user)

        if book_notes and user.id == book_notes.values()[0].get('user_id'):
                text_value = book_notes.values()[0].get('text')
                context['UserBookNotesFormSet'] = self.UserBookNotesFormSet({'text': text_value})
        else:
            context['UserBookNotesFormSet'] = self.UserBookNotesFormSet()
        context['AddUpdateBookForm'] = AddUpdateBookForm
        return context


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = "/" #will redirect to home page on successful deletion