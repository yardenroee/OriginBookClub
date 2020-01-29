from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from bookclub.models import Book
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')
    favorites = models.ManyToManyField(Book, related_name='favorited_by')
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)