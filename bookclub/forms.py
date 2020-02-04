from .models import Book, UserBookNotes, Comment
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
        widgets = {
          'text': forms.Textarea(attrs={'rows':5, 'cols':1}),
        }
    def __init__(self, *args, **kwargs):
        super(BookNoteUpdateForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'My Notes:'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
          'text': forms.Textarea(attrs={'rows':3, 'cols':1}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = 'Add a comment:'
