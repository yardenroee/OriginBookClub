# Generated by Django 3.0.2 on 2020-01-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0003_auto_20200129_0047'),
        ('users', '0004_remove_profile_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='bookclub.Book'),
        ),
    ]
