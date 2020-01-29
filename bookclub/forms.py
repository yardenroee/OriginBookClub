from .models import Book
from django import forms

class AddBookForm(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()
    genre = forms.ChoiceField(choices=Book.GENRE_CHOICES)
    notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'No worries if you have nothing yet, you can always edit this later!'}))
    year = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Book
        fields= ['title','author','genre','notes','year','image']

class UpdateBookForm(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()
    genre = forms.ChoiceField(choices=Book.GENRE_CHOICES)
    notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'No worries if you have nothing yet, you can always edit this later!'}))
    year = forms.CharField()
    image = forms.ImageField()
    class Meta:
        model = Book
        fields= ['title','author','genre','notes','year','image']