# Generated by Django 3.0.2 on 2020-01-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0011_auto_20200130_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
