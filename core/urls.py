# core/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        'mensaje': 'Bienvenido a la API de Productos',
        'endpoints': {
            'productos': '/api/productos/',
            'admin': '/admin/',
        }
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', api_root, name='api_root'),
    path('', include('productos.urls')),  # ← ESTA LÍNEA ES CLAVE
]