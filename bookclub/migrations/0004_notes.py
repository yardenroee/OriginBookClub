# Generated by Django 3.0.2 on 2020-01-30 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0003_auto_20200129_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
        ),
    ]