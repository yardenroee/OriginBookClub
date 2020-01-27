# Generated by Django 3.0 on 2020-01-27 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[("Children's", "Children's"), ('Action', 'Action'), ('Romance', 'Romance'), ('Spirituality', 'Spirituality'), ('Fiction(other)', 'Fiction(other)'), ('Non-fiction(other)', 'Non-fiction(other)')], default='Non-fiction(other)', max_length=100)),
                ('notes', models.TextField()),
                ('year', models.CharField(max_length=4)),
            ],
        ),
    ]