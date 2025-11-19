# productos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crear router y registrar ViewSet
router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='producto')

# URLs de la API
urlpatterns = [
    path('api/', include(router.urls)),
]