# Generated by Django 3.0.2 on 2020-01-30 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookclub', '0012_auto_20200130_0612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='notes',
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('notes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookclub.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
