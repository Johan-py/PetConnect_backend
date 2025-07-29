from django.db import models
import uuid

# Create your models here.
class Citas(models.Model):
    id_cita = models.CharField(max_length=32, unique=True, editable=False)
    fecha = models.DateTimeField()
    contexto = models.TextField()
    estado = models.CharField(max_length=20, default='programada', choices=[
        ('programada','Programada'),
        ('cancelada', 'Cancelada'),
        ('completada','Completada')
    ])
    creado_en = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **Kwargs):
        if not self.id_cita:
            self.id_cita = uuid.uuid4().hex
        super().save(*args, **Kwargs)
    def __str__(self):
        return f'Cita el {self.fecha.strftime("%Y-%m-%d %H:%M")}'
    