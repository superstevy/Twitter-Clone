from django.db import models
from cloudinary.models import CloudinaryField


class Tweet(models.Model):
    image = CloudinaryField('image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.ManyToManyField('self', related_name='likes')
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=14)
    body = models.CharField(max_length=140)

    def total_likes(self):
        return self.like_count.count()
