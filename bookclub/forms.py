from .models import Book, UserBookNotes
from django import forms

class AddUpdateBookForm(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()
    genre = forms.ChoiceField(choices=Book.GENRE_CHOICES)
    about = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'A little overview about this book'}))
    year = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Book
        fields= ['title','author','genre','about','year','image']

class BookNoteUpdateForm(forms.ModelForm):
    class Meta:
        model = UserBookNotes
        fields = ['text']