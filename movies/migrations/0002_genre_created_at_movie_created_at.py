# Generated by Django 4.2 on 2023-04-20 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 12, 41, 6, 283535, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 20, 12, 41, 6, 283757, tzinfo=datetime.timezone.utc)),
        ),
    ]
