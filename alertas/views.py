from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import AlertaService

class AlertaCreateAPIView(APIView):
    def post(self, request):
        try:
            alerta = AlertaService.crear_alerta(
                tipo=request.data.get('tipo'),
                contexto=request.data.get('contexto')
            )
            return Response(
                {"id_alerta": str(alerta.id_alerta), "tipo": alerta.tipo},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

class AlertaDeleteAPIView(APIView):
    def delete(self, request, alerta_id):
        try:
            AlertaService.eliminar_alerta(alerta_id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
