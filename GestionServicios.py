from abc import ABC, abstractmethod

class iservicioprograma(ABC):
    @abstractmethod
    def realizar_servicio(self):
        pass
    @abstractmethod
    def imprimir_servicio(self):
        pass

class GestionServicios():
    def __init__(self):
        self.Servicioprograma = self.Servicioprograma()
        self.Serviciotargeta = self.Serviciotargeta()
        self.Servicioseguro = self.Servicioseguro()

    class Servicioprograma(iservicioprograma, ABC):
        def __init__(self):
            self.programas = []

        def realizar_servicio(self):
            nombre_programa = input("Nombre del programa: ")
            tipo_programa = input("Tipo de programa: ")
            fecha_inicio = input("Fecha de inicio: ")

            programa = {
                'nombre_programa': nombre_programa,
                'tipo_programa': tipo_programa,
                'fecha_inicio': fecha_inicio
            }

            self.programas.append(programa)

        def imprimir_servicio(self):
            for programa in self.programas:
                print(programa)

    class Serviciotargeta(iservicioprograma, ABC):
        def __init__(self):
            self.tarjetas = []

        def realizar_servicio(self):
            cvv = int(input("Nombre de la tarjeta: "))
            año_e = input("Tipo de tarjeta: ")
            mes_m = input("Fecha de vencimiento: ")
            fehca_v = input("Fecha de vencimiento: ")
            numero = input("Numero targeta: ")
            zip = input("Zip code: ")

            targeta = {
                'cvv': cvv,
                'año_e': año_e,
                'mes_m': mes_m,
                'fehca_v': fehca_v,
                'numero': numero,
                'zip': zip
            }

            self.tarjetas.append(targeta)

        def imprimir_servicio(self):
            for targeta in self.tarjetas:
                print(targeta)

    class Servicioseguro(iservicioprograma, ABC):
        def __init__(self):
            self.seguros = []

        def realizar_servicio(self):
            nombre_seguro = input("Nombre del seguro: ")
            tipo_seguro = input("Tipo de seguro: ")
            fecha_inicio = input("Fecha de inicio: ")
            fecha_vencimiento = input("Fecha de vencimiento: ")
            estado = input("Estado: ")
            
            seguro = {
                'nombre_seguro': nombre_seguro,
                'tipo_seguro': tipo_seguro,
                'fecha_inicio': fecha_inicio,
                'fecha_vencimiento': fecha_vencimiento,
                'estado': estado
            }
            self.seguros.append(seguro)

        def imprimir_servicio(self):
            for seguro in self.seguros:
                print(seguro)