# Generated by Django 3.0.2 on 2020-01-29 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0003_auto_20200129_0047'),
        ('users', '0002_auto_20200127_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(to='bookclub.Book'),
        ),
    ]
