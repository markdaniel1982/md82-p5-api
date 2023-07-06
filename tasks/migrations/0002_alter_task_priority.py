# Generated by Django 3.2.19 on 2023-07-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(1, 'URGENT'), (2, 'Normal'), (3, 'Low')], default=2),
        ),
    ]