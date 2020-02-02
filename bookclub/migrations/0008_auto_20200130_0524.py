# Generated by Django 3.0.2 on 2020-01-30 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0007_auto_20200130_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='notes',
        ),
        migrations.AlterField(
            model_name='book',
            name='about',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookclub.Book'),
        ),
    ]