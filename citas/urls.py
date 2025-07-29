from django.urls import path
from .views import CitaCreateAPIView

urlpatterns = [ 
    path('crear/', CitaCreateAPIView.as_view(), name='crear_cita'),
]