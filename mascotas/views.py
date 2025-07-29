from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import MascotaService
from .serializers import MascotaSerializer

class MascotaCreateAPIView(APIView):
    def post(self, request):
        try:
            mascota = MascotaService.crear_mascota(
                nombre=request.data.get('nombre'),
                especie=request.data.get('especie'),
            )
            
            serializer = MascotaSerializer(mascota)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class MascotaDeleteAPIView(APIView):
    def delete(self, request, id_mascota):
        try:
            MascotaService.eliminar_mascota(id_mascota)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )

class MascotaListAPIView(APIView):
    def get(self, request):
        try:
            mascotas = MascotaService.obtener_todas_mascotas()
            serializer = MascotaSerializer(mascotas, many=True)
            return Response({
                "count": len(serializer.data),
                "mascotas": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )