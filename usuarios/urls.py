from django.urls import path
from .views import UsuarioCreateAPIView, UsuarioDeleteAPIView

urlpatterns = [
    path('crear/', UsuarioCreateAPIView.as_view(), name='crear-usuario'),
    path('eliminar/<str:id_usuario>/', UsuarioDeleteAPIView.as_view(), name='eliminar-usuario'),
]