from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    
    def get_absolute_url(self):
        return reverse('Post-Detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f"""
[{self.title}] posteado por {self.author.username}
el {self.date_posted.strftime('%d-%m-%Y %H:%M:%S')}
"""

