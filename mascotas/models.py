from django.db import models
import uuid
from usuarios.models import Usuario 

# Create your models here.
class Mascota(models.Model):
    id_mascota = models.CharField(max_length=32, unique=True, editable=False)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id_mascota:
            self.id_mascota = uuid.uuid4().hex
        super().save(*args, **kwargs)

