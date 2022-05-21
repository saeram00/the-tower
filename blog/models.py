from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    
