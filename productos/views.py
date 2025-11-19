from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de productos.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # def list(self, request):
    #     """
    #     Lista todos los productos disponibles
    #     """
    #     productos = self.get_queryset()
    #     serializer = self.get_serializer(productos, many=True)
    #     return Response({
    #         'count': productos.count(),
    #         'productos': serializer.data
    #     })
    
    # def create(self, request):
    #     """
    #     Crea un nuevo producto
    #     """
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             {'mensaje': 'Producto creado exitosamente', 'producto': serializer.data},
    #             status=status.HTTP_201_CREATED
    #         )
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def retrieve(self, request, pk=None):
    #     """
    #     Obtiene un producto específico por ID
    #     """
    #     try:
    #         producto = self.get_object()
    #         serializer = self.get_serializer(producto)
    #         return Response(serializer.data)
    #     except Producto.DoesNotExist:
    #         return Response(
    #             {'error': 'Producto no encontrado'}, 
    #             status=status.HTTP_404_NOT_FOUND
    #         )

# AGREGAR ESTAS CLASES AL FINAL DEL ARCHIVO - JWT AUTHENTICATION
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)