from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogUser(models.Model):

    nombre_usuario = models.CharField(max_length=60)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"""
Username: {nombre_usuario}
Creado en: {fecha_registro}
"""
