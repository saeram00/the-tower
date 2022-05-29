from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Profile(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_usuario = models.CharField(max_length=60)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(default=timezone.now)
    foto_perfil = models.ImageField(default='default.jpg',
                                    upload_to='profile-pics')

    def save(self):
        super().save()
        prof_pic = Image.open(self.foto_perfil.path)
        if prof_pic.height > 250 or prof_pic.width > 250:
            output_size = (250, 250)
            prof_pic.thumbnail(output_size)
            prof_pic.save(self.foto_perfil.path)

    def get_absolute_url(self):
        return reverse('Userdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"""
{self.usuario.username}
Creado el: {self.fecha_registro.strftime('%d-%m-%Y %H:%M:%S')}
"""

