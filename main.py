# Clase Activo
class Activo:
    def __init__(self, nombre, categoria, fecha_adquisicion):
        self.nombre = nombre
        self.categoria = categoria
        self.fecha_adquisicion = fecha_adquisicion

# Lista de activos
activos = []

# Función para registrar activos
def registrar_activo(nombre, categoria, fecha_adquisicion):
    nuevo_activo = Activo(nombre, categoria, fecha_adquisicion)
    activos.append(nuevo_activo)

# Función para listar activos
def listar_activos():
    for activo in activos:
        print(f"Nombre: {activo.nombre}, Categoría: {activo.categoria}, Fecha de Adquisición: {activo.fecha_adquisicion}")

# Función para editar un activo existente (Historia de Usuario 3)
def editar_activo(nombre, nuevo_nombre=None, nueva_categoria=None, nueva_fecha=None):
    for activo in activos:
        if activo.nombre == nombre:
            if nuevo_nombre:
                activo.nombre = nuevo_nombre
            if nueva_categoria:
                activo.categoria = nueva_categoria
            if nueva_fecha:
                activo.fecha_adquisicion = nueva_fecha
            print(f"El activo '{nombre}' ha sido actualizado.")
            return
    print(f"Activo con nombre '{nombre}' no encontrado.")

# Función para buscar un activo por nombre
def buscar_activo(nombre_buscar):
    for activo in activos:
        if nombre_buscar.lower() in activo.nombre.lower():
            print(f"Nombre: {activo.nombre}, Categoría: {activo.categoria}, Fecha de Adquisición: {activo.fecha_adquisicion}")

# Función para eliminar un activo
def eliminar_activo(nombre):
    global activos
    activos = [activo for activo in activos if activo.nombre != nombre]
    print(f"El activo '{nombre}' ha sido eliminado.")

# Menú principal
if __name__ == "__main__":
    while True:
        print("\nGestión de Activos")
        print("1. Registrar Activo")
        print("2. Listar Activos")
        print("3. Editar Activo")
        print("4. Buscar Activo")
        print("5. Eliminar Activo")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del activo: ")
            categoria = input("Categoría del activo: ")
            fecha = input("Fecha de adquisición (DD-MM-AAAA): ")
            registrar_activo(nombre, categoria, fecha)
        elif opcion == "2":
            listar_activos()
        elif opcion == "3":
            nombre = input("Nombre del activo a editar: ")
            nuevo_nombre = input("Nuevo nombre (presiona Enter para no cambiar): ")
            nueva_categoria = input("Nueva categoría (presiona Enter para no cambiar): ")
            nueva_fecha = input("Nueva fecha de adquisición (presiona Enter para no cambiar): ")
            editar_activo(nombre, nuevo_nombre or None, nueva_categoria or None, nueva_fecha or None)
        elif opcion == "4":
            nombre_buscar = input("Nombre del activo a buscar: ")
            buscar_activo(nombre_buscar)
        elif opcion == "5":
            nombre = input("Nombre del activo a eliminar: ")
            eliminar_activo(nombre)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
# main.py
activos = {}

def agregar_activo(id_activo, nombre, tipo, ubicacion):
    activos[id_activo] = {
        "nombre": nombre,
        "tipo": tipo,
        "ubicacion": ubicacion
    }
    print(f"Activo {nombre} agregado correctamente.")

def editar_activo(id_activo, nuevo_nombre=None, nuevo_tipo=None, nueva_ubicacion=None):
    if id_activo in activos:
        if nuevo_nombre:
            activos[id_activo]["nombre"] = nuevo_nombre
        if nuevo_tipo:
            activos[id_activo]["tipo"] = nuevo_tipo
        if nueva_ubicacion:
            activos[id_activo]["ubicacion"] = nueva_ubicacion
        print(f"Activo {id_activo} editado correctamente.")
    else:
        print("El activo no existe.")

def consultar_activo(id_activo):
    if id_activo in activos:
        print(f"Detalles del activo {id_activo}: {activos[id_activo]}")
    else:
        print("El activo no existe.")

def eliminar_activo(id_activo):
    if id_activo in activos:
        del activos[id_activo]
        print(f"Activo {id_activo} eliminado correctamente.")
    else:
        print("El activo no existe.")

# Ejemplo de uso
if __name__ == "__main__":
    agregar_activo(1, "Computadora", "Electrónica", "Oficina A")
    consultar_activo(1)
    editar_activo(1, nueva_ubicacion="Oficina B")
    consultar_activo(1)
    eliminar_activo(1)
    consultar_activo(1)
