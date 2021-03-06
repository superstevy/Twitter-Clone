# Generated by Django 3.1.7 on 2021-03-31 02:55

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_auto_20210327_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='like_count',
        ),
        migrations.AddField(
            model_name='tweet',
            name='like_count',
            field=models.ManyToManyField(blank=True, related_name='_tweet_like_count_+', to='twitter.Tweet'),
        ),
    ]
