from rest_framework import serializers
from .models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['id_mascota', 'nombre', 'especie']
        read_only_fields = ['id_mascota']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation