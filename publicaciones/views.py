from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import PublicacionService
from .serializers import PublicacionSerializer

class PublicacionCreateAPIView(APIView):
    def post(self, request):
        try:
            publicacion = PublicacionService.crear_publicacion(
                usuario_id=request.data.get('usuario'),
                mascota_id=request.data.get('mascota'),
                descripcion=request.data.get('descripcion')
            )
            serializer = PublicacionSerializer(publicacion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PublicacionDeleteAPIView(APIView):
    def delete(self, request, publicacion_id):
        try:
            PublicacionService.eliminar_publicacion(publicacion_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)


class PublicacionListAPIView(APIView):
    def get(self, request):
        try:
            publicaciones = PublicacionService.listar_publicaciones()
            serializer = PublicacionSerializer(publicaciones, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
