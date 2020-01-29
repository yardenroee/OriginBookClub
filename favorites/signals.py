from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Favorites

@receiver(post_save, sender=User) # on creation of user will trigger favorite list creation
def create_favorites(sender, instance, created, **kwargs):
    if created:
        favorites = Favorites.objects.create(user = instance) #the instance that will trigger the creation of the favs
        favorites.save()