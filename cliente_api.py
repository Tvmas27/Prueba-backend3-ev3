# cliente_compacto.py
import requests

def registrar_usuario():
    print("\n📝 REGISTRAR USUARIO")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    
    try:
        resp = requests.post("http://localhost:8000/api/auth/register/",
                           json={"username": username, "password": password, "password_confirm": password})
        if resp.status_code == 201:
            print("✅ Usuario creado!")
            return resp.json()['access']
        else:
            print("❌ Error:", resp.text)
    except:
        print("❌ Error de conexión")

def iniciar_sesion():
    print("\n🔐 INICIAR SESIÓN")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    
    try:
        resp = requests.post("http://localhost:8000/api/auth/login/",
                           json={"username": username, "password": password})
        if resp.status_code == 200:
            print("✅ Login exitoso!")
            return resp.json()['access']
        else:
            print("❌ Credenciales incorrectas")
    except:
        print("❌ Error de conexión")

def main():
    token = None
    
    while not token:
        print("\n🚀 CLIENTE JWT")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        opcion = input("Opción: ")
        
        if opcion == "1":
            token = iniciar_sesion()
        elif opcion == "2":
            token = registrar_usuario()
    
    # Menú principal
    while True:
        print("\n🏪 MENÚ")
        print("1. Ver productos")
        print("2. Crear producto")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Opción: ")
        
        headers = {"Authorization": f"Bearer {token}"}
        
        if opcion == "1":
            resp = requests.get("http://localhost:8000/api/productos/", headers=headers)
            if resp.status_code == 200:
                for p in resp.json():
                    print(f" {p['id']}: {p['nombre']} - ${p['precio']}")
        
        elif opcion == "2":
            nombre = input("Nombre: ")
            precio = input("Precio: ")
            stock = input("Stock: ")
            
            resp = requests.post("http://localhost:8000/api/productos/", 
                               json={"nombre": nombre, "precio": precio, "stock": stock},
                               headers=headers)
            if resp.status_code == 201:
                print("✅ Producto creado!")
        
        elif opcion == "3":
            id_producto = input("ID del producto a editar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            
            resp = requests.patch(f"http://localhost:8000/api/productos/{id_producto}/", 
                                json={"nombre": nuevo_nombre},
                                headers=headers)
            if resp.status_code == 200:
                print("✅ Producto editado!")
        
        elif opcion == "4":
            id_producto = input("ID del producto a eliminar: ")
            
            resp = requests.delete(f"http://localhost:8000/api/productos/{id_producto}/", 
                                 headers=headers)
            if resp.status_code == 204:
                print("✅ Producto eliminado!")
        
        elif opcion == "5":
            print("👋 Adiós!")
            break

if __name__ == "__main__":
    main()