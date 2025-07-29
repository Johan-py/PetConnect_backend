from .models import Usuario
from django.core.exceptions import ValidationError
import uuid

class UsuarioService:
    @staticmethod
    def crear_usuario(nombre, ci):
        try:
            if Usuario.objects.filter(ci=ci).exists():
                raise ValidationError("Ya existe un usuario con este CI")

            usuario = Usuario.objects.create(
                id_usuario=uuid.uuid4().hex,
                nombre=nombre,
                ci=ci
            )
            return usuario
        except ValidationError as ve:
            raise ve
        except Exception as e:
            raise ValidationError(f"Error inesperado al crear usuario: {str(e)}")

    @staticmethod
    def eliminar_usuario(usuario_id):
        try:
            usuario = Usuario.objects.get(id_usuario=usuario_id)
            usuario.delete()
            return True
        except Usuario.DoesNotExist:
            raise ValidationError("Usuario no encontrado")
