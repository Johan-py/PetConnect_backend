from .models import Alerta
from django.core.exceptions import ValidationError

class AlertaService:
    @staticmethod
    def crear_alerta(tipo, contexto):
        try:
            alerta = Alerta.objects.create(
                tipo=tipo,
                contexto=contexto
            )
            AlertaService._notificar_usuarios(alerta)
            return alerta
        except Exception as e:
            raise ValidationError(f"Error al crear alerta: {e}")
        
    @staticmethod
    def eliminar_alerta(alerta_id):
        try:
            alerta = Alerta.objects.get(id_alerta=alerta_id)  # ✅ corregido
            alerta.delete()
            return True
        except Alerta.DoesNotExist:
            raise ValidationError("Alerta no encontrada")
        except Exception as e:
            raise ValidationError(f"Error al eliminar alerta: {e}")
        
    @staticmethod
    def _notificar_usuarios(alerta):
        print(f"📢 Notificación enviada: alerta {alerta.tipo}")
