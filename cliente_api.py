# cliente_api.py
import requests

class ClienteAPI:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.token = None
    
    def login(self, usuario="usuario_prueba", clave="password123"):
        """Login simple"""
        datos = {"username": usuario, "password": clave}
        try:
            response = requests.post(f"{self.base_url}/api/auth/login/", json=datos)
            if response.status_code == 200:
                self.token = response.json()['access']
                print("✅ Login exitoso")
                return True
            else:
                print("❌ Login falló")
                return False
        except:
            print("❌ Servidor no disponible")
            return False
    
    def registrar(self, usuario="usuario_prueba", email="prueba@test.com", clave="password123"):
        """Registro simple"""
        datos = {
            "username": usuario, 
            "email": email, 
            "password": clave, 
            "password_confirm": clave
        }
        response = requests.post(f"{self.base_url}/api/auth/register/", json=datos)
        if response.status_code == 201:
            print("✅ Usuario registrado")
            return True
        else:
            print("⚠️ Usuario ya existe o error")
            return False
    
    def obtener_productos(self):
        """Obtener productos - corregido para manejar lista directa"""
        if not self.token:
            print("❌ Necesitas login primero")
            return []
        
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(f"{self.base_url}/api/productos/", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            
            # Manejar tanto lista directa como objeto con 'results'
            if isinstance(data, list):
                productos = data
            else:
                productos = data.get('results', [])
            
            print(f"📦 {len(productos)} productos encontrados")
            return productos
        else:
            print(f"❌ Error: {response.status_code}")
            return []
    
    def crear_producto(self, nombre, precio, stock=0):
        """Crear producto simple"""
        if not self.token:
            print("❌ Necesitas login primero")
            return False
        
        headers = {'Authorization': f'Bearer {self.token}'}
        datos = {
            "nombre": nombre,
            "precio": precio,
            "stock": stock,
            "disponible": True
        }
        
        response = requests.post(f"{self.base_url}/api/productos/", json=datos, headers=headers)
        
        if response.status_code == 201:
            print(f"✅ Producto '{nombre}' creado")
            return True
        else:
            print(f"❌ Error creando producto: {response.text}")
            return False

# Uso rápido
if __name__ == "__main__":
    cliente = ClienteAPI()
    
    # 1. Registrar usuario (solo primera vez)
    cliente.registrar()
    
    # 2. Login
    if cliente.login():
        # 3. Crear productos
        cliente.crear_producto("Laptop", 1000, 5)
        cliente.crear_producto("Mouse", 25, 10)
        
        # 4. Listar productos
        productos = cliente.obtener_productos()
        for p in productos:
            print(f"🎯 {p['id']}: {p['nombre']} - ${p['precio']}")