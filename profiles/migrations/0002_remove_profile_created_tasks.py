# Generated by Django 3.2.19 on 2023-07-05 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created_tasks',
        ),
    ]
