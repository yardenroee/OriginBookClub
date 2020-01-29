from django.db import models
from PIL import Image
from django.urls import reverse
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
    about = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(default='default_cover.jpg', upload_to="cover_pics")
    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk' : self.pk})