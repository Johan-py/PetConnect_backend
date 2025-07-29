from django.urls import path
from .views import (
    PublicacionCreateAPIView,
    PublicacionListAPIView,
    PublicacionDeleteAPIView
)

urlpatterns = [
    path('crear/', PublicacionCreateAPIView.as_view(), name='crear-publicacion'),
    path('publicaciones/', PublicacionListAPIView.as_view(), name='listar-publicaciones'),
    path('eliminar/<str:publicacion_id>/', PublicacionDeleteAPIView.as_view(), name='eliminar-publicacion'),
]


