from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Message(models.Model):

    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    destinatario = models.CharField(max_length=60)
    fecha_emision = models.DateTimeField(default=timezone.now)
    asunto = models.CharField(max_length=120)
    contenido = models.TextField()

    def get_absolute_url(self):
        return reverse('Chat-Detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"""
[ De: {self.remitente} ]
[ Para: {self.destinatario} ]
[ Fecha: {self.fecha_emision.strftime('%d-%m-%Y %H:%M:%S')} ]
[ Asunto: {self.asunto} ]
"""

