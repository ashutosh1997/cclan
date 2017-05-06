# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.TextField(blank=True)
    post_image = models.ImageField(upload_to='post_image/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.post_text

