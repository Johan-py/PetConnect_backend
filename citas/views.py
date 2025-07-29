from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .services import CitasService
from datetime import datetime

class CitaCreateAPIView(APIView):
    def post(self, request):
        try:
            fecha_str = request.data.get('fecha')
            contexto = request.data.get('contexto')
            estado = request.data.get('estado', 'programada')

            if not fecha_str or not contexto:
                raise ValueError("Los campos 'fecha' y 'contexto' son requeridos")

            # convertir la fecha recibida a objeto datetime
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")

            cita = CitasService.crear_cita(
                fecha=fecha,
                contexto=contexto,
                estado=estado
            )

            return Response({
                "id": cita.id_cita,
                "fecha": cita.fecha,
                "contexto": cita.contexto,
                "estado": cita.estado,
                "mensaje": "Cita creada exitosamente"
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {
                    "error": str(e),
                    "detalle": "Revise los datos enviados",
                    "ejemplo_valido": {
                        "fecha": "2025-12-25 15:30",
                        "contexto": "Control anual",
                        "estado": "programada"
                    }
                },
                status=status.HTTP_400_BAD_REQUEST
            )
