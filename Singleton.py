class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("⏳ Inicializando la conexión a la base de datos...")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Aquí irían las credenciales y lógica de conexión real
            cls._instance.status = "Conectado"
        
        return cls._instance

conexion_usuarios = DatabaseConnection()
conexion_productos = DatabaseConnection()

print(f"ID en memoria (Usuarios): {id(conexion_usuarios)}")
print(f"ID en memoria (Productos): {id(conexion_productos)}")
print(f"¿Son exactamente el mismo objeto? {conexion_usuarios is conexion_productos}")