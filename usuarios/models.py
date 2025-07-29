from django.db import models
import uuid
# Create your models here.
class Usuario(models.Model):
    id_usuario = models.CharField(max_length=32, unique=True, editable=False)
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        if not self.id_usuario:
            self.id_usuario = uuid.uuid4().hex
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.nombre} ({self.ci})'
    
