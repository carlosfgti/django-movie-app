# Generated by Django 4.2 on 2023-04-20 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_genre_created_at_movie_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
