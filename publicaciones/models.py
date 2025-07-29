from django.db import models
from usuarios.models import Usuario
from mascotas.models import Mascota
import uuid

# Función helper para usar como default
def generate_uuid_hex():
    return uuid.uuid4().hex

class Publicacion(models.Model):
    id_publicacion = models.CharField(
        max_length=32,
        primary_key=True,
        default=generate_uuid_hex,
        editable=False
    )
    usuario = models.ForeignKey(
        Usuario, on_delete=models.CASCADE,
        related_name="publicaciones", to_field='id_usuario'
    )
    mascota = models.ForeignKey(
        Mascota, on_delete=models.CASCADE,
        related_name="publicaciones", to_field='id_mascota'
    )
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id_publicacion:
            self.id_publicacion = generate_uuid_hex()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Publicación #{self.id_publicacion} - {self.mascota.nombre}"
