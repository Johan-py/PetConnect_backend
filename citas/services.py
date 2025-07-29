from .models import Citas
from django.core.exceptions import ValidationError
import uuid
from datetime import datetime

class CitasService:
    @staticmethod
    def crear_cita(fecha, contexto, estado='programada'):
        try:
            cita = Citas(
                id_cita=uuid.uuid4().hex,
                fecha=fecha,
                contexto=contexto,
                estado=estado
            )
            cita.save()
            return cita
        except Exception as e:
            raise ValidationError(f"Error al crear cita: {str(e)}")
    
    @staticmethod
    def cancelar_cita(cita_id):
        try:
            cita = Citas.objects.get(id_cita=cita_id)
            
            if cita.estado == 'cancelada':
                raise ValidationError('La cita ya está cancelada')
            if cita.estado == 'completada':
                raise ValidationError('No se puede cancelar una cita completada')
            
            cita.estado = 'cancelada'
            cita.save()
            return cita
        except Citas.DoesNotExist:
            raise ValidationError('Cita no encontrada')
        except Exception as e:
            raise ValidationError(f'Error al cancelar cita: {str(e)}')
