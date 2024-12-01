class Activo:
    def __init__(self, nombre, categoria, fecha_adquisicion):
        self.nombre = nombre
        self.categoria = categoria
        self.fecha_adquisicion = fecha_adquisicion

activos = []

def registrar_activo(nombre, categoria, fecha_adquisicion):
    nuevo_activo = Activo(nombre, categoria, fecha_adquisicion)
    activos.append(nuevo_activo)
