from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id_usuario", "nombre", "ci"]
        read_only_fields = ["id_usuario"]
