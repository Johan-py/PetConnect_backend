from django.urls import path
from .views import MascotaCreateAPIView, MascotaDeleteAPIView, MascotaListAPIView

urlpatterns = [
    path('crear/', MascotaCreateAPIView.as_view(), name='crear-mascota'),
    path('eliminar/<str:id_mascota>/', MascotaDeleteAPIView.as_view(), name='eliminar-mascota'),
    path('mascotas/', MascotaListAPIView.as_view(), name='listar-mascotas'),
]