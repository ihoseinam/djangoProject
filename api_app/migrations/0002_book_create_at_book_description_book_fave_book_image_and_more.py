# Generated by Django 5.0.6 on 2024-05-14 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='fave',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='store_image/'),
        ),
        migrations.AddField(
            model_name='book',
            name='store_name',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default=False, max_length=150),
        ),
    ]