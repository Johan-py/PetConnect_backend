from .models import Mascota
from django.core.exceptions import ValidationError
from typing import List

class MascotaService:
    @staticmethod
    def crear_mascota(nombre, especie) -> Mascota:
        try:
            
            mascota = Mascota(
                nombre=nombre,
                especie=especie,
            )
            mascota.save()
            return mascota
            
        except Mascota.DoesNotExist:
            raise ValidationError(f"No existe usuario con ID: {mascota.id_mascota}")
        except Exception as e:
            raise ValidationError(f"Error al crear mascota: {str(e)}")

        

    @staticmethod
    def eliminar_mascota(id_mascota):
        try:
            mascota = Mascota.objects.get(id_mascota=id_mascota)
            mascota.delete()
            return True
        except Mascota.DoesNotExist:
            raise ValidationError("Mascota no encontrada")
    

    @staticmethod
    def obtener_todas_mascotas() -> List[Mascota]:

        return Mascota.objects.all().order_by('nombre')