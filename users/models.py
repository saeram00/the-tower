from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):

    nombre_usuario = models.CharField(max_length=60)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(default=timezone.now)
    foto_perfil = models.ImageField(default='default.jpg',
                                    upload_to='profile-pics')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"""
{self.nombre_usuario}
Creado el: {self.fecha_registro.strftime('%d-%m-%Y %H:%M:%S')}
"""
