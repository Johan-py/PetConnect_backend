from django.db import models
import uuid

class Alerta(models.Model):
    id_alerta = models.CharField(max_length=32, unique=True, editable=False)
    contexto = models.TextField()
    tipo = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)  
    activa = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id_alerta:
            self.id_alerta = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Alerta {self.tipo}'
