# Generated by Django 3.0.2 on 2020-01-30 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookclub', '0013_auto_20200130_0633'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookclub.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ManyToManyField(related_name='books', through='bookclub.UserBookNotes', to=settings.AUTH_USER_MODEL),
        ),
    ]