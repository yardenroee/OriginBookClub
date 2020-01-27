from django.db import models

class Book(models.Model):
    GENRE_CHOICES = [
        ("Children's", "Children's"),
        ("Action","Action"),
        ("Romance", "Romance"),
        ("Spirituality", "Spirituality"),
        ("Fiction(other)","Fiction(other)"),
        ("Non-fiction(other)", "Non-fiction(other)")
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default="Non-fiction(other)")
    notes = models.TextField()
    year = models.CharField(max_length=4)
