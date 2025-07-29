from django.core.exceptions import ValidationError
from .models import Publicacion
import uuid

class PublicacionService:
    @staticmethod
    def crear_publicacion(usuario_id, mascota_id, descripcion):
        try:
            publicacion = Publicacion.objects.create(
                id_publicacion=uuid.uuid4().hex,
                usuario_id=usuario_id,
                mascota_id=mascota_id,
                descripcion=descripcion
            )
            return publicacion
        except Exception as e:
            raise ValidationError(f'Error al crear publicación: {str(e)}')

    @staticmethod
    def eliminar_publicacion(publicacion_id):
        try:
            publicacion = Publicacion.objects.get(id_publicacion=publicacion_id)
            publicacion.activa = False
            publicacion.save()
            return True
        except Publicacion.DoesNotExist:
            raise ValidationError("Publicación no encontrada")

    @staticmethod
    def listar_publicaciones():
        try:
            return Publicacion.objects.filter(activa=True).order_by('-fecha_creacion')
        except Exception as e:
            raise ValidationError(f'Error al obtener publicaciones: {str(e)}')
