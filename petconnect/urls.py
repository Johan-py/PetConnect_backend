
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/alertas/', include('alertas.urls')),
    path('api/citas/', include('citas.urls')),
    path('api/publicacion/', include('publicaciones.urls')),
    path('api/usuario/', include('usuarios.urls')),
    path('api/mascota/', include('mascotas.urls'))
]
