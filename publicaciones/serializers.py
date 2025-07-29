from rest_framework import serializers
from .models import Publicacion

class PublicacionSerializer(serializers.ModelSerializer):
    usuario_info = serializers.SerializerMethodField()
    mascota_info = serializers.SerializerMethodField()

    class Meta:
        model = Publicacion
        fields = ['id_publicacion', 'usuario_info', 'mascota_info', 
                 'descripcion', 'fecha_creacion', 'activa']
    
    def get_usuario_info(self, obj):
        try:
            return {
                "id": str(obj.usuario.id_usuario),
                "nombre": obj.usuario.nombre
            }
        except:
            return None
    
    def get_mascota_info(self, obj):
        try:
            return {
                "id": str(obj.mascota.id_mascota),
                "nombre": obj.mascota.nombre
            }
        except:
            return None