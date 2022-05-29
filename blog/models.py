from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    foto_post = models.ImageField(default='default-post.jpg',
                                  upload_to='post-pics')
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    
    def save(self):
        super().save()
        upload = Image.open(self.foto_post.path)
        if upload.height > 200 or upload.width > 200:
            output_size = (200, 200)
            upload.thumbnail(output_size)
            upload.save(self.foto_post.path)

    def get_absolute_url(self):
        return reverse('Post-Detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return f"""
[{self.title}] posteado por {self.author.username}
el {self.date_posted.strftime('%d-%m-%Y %H:%M:%S')}
"""

