from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='producto')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/login/', views.CustomTokenObtainPairView.as_view(), name='login'),
    path('api/auth/register/', views.RegisterView.as_view(), name='register'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/profile/', views.ProfileView.as_view(), name='profile'),
]