from django.urls import path
from .views import AlertaCreateAPIView, AlertaDeleteAPIView

urlpatterns = [
    path('crear/', AlertaCreateAPIView.as_view(), name='crear-alerta'),
    path('eliminar/<str:alerta_id>', AlertaDeleteAPIView.as_view(), name= 'eliminar-alerta'),
]