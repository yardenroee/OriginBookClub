from .models import Book
from django import forms

class AddBookForm(forms.ModelForm):
    title = forms.CharField()
    author = forms.CharField()
    genre = forms.ChoiceField()
    notes = forms.Textarea()
    year = forms.ChoiceField()
    image = forms.ImageField()
    class Meta:
        model = Book
        fields= ['title','author','genre','notes','year','image']