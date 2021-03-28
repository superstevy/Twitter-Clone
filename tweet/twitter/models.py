from django.db import models
from cloudinary.models import CloudinaryField


class Tweet(models.Model):
    image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=14)
    body = models.CharField(max_length=140)
