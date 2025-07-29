from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import UsuarioService
from .serializers import UsuarioSerializer
from django.core.exceptions import ValidationError

class UsuarioCreateAPIView(APIView):
    def post(self, request):
        try:
            nombre = request.data.get("nombre")
            ci = request.data.get("ci")

            if not nombre or not ci:
                return Response(
                    {"error": "Nombre y CI son obligatorios"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            usuario = UsuarioService.crear_usuario(nombre=nombre, ci=ci)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Error interno: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UsuarioDeleteAPIView(APIView):
    def delete(self, request, id_usuario):
        try:
            UsuarioService.eliminar_usuario(id_usuario)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
