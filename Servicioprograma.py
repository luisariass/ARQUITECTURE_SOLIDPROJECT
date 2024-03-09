from abc import ABC
#from datetime import date
#from iservicio import IGestionServicios

class iservicioprograma(ABC):
    def realizar_servicio_programa(self):
        pass
    def imprimir_servicio_programa(self):
        pass

class Servicioprograma(iservicioprograma, ABC):
    def __init__(self):
        self.programas = []

    def agregar_programa(self):
        nombre_programa = input("Nombre del programa: ")
        tipo_programa = input("Tipo de programa: ")
        fecha_inicio = input("Fecha de inicio: ")

        programa = {
            'nombre_programa': nombre_programa,
            'tipo_programa': tipo_programa,
            'fecha_inicio': fecha_inicio
        }

        self.programas.append(programa)

    def mostrar_programas(self):
        for programa in self.programas:
            print(programa)

class Serviciotargeta(iservicioprograma, ABC):
    def realizar_servicio_targeta(self):
        print("Agendando tarjeta")
        nombre_tarjeta = input("Nombre de la tarjeta: ")
        tipo_tarjeta = input("Tipo de tarjeta: ")
        fecha_vencimiento = input("Fecha de vencimiento: ")
        return f"Tarjeta agendada: {nombre_tarjeta}, {tipo_tarjeta}, {fecha_vencimiento}"

    def imprimir_servicio_targeta(self):
        pass