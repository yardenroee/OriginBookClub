from django.db import models
from bookclub.models import Book
from django.contrib.auth.models import User
# Create your models here.

class Favorites(models.Model):
    books = models.ManyToManyField(Book)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} favorites'