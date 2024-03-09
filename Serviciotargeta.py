from datetime import date
from iservicio import IGestionServicios

class Serviciotargeta(IGestionServicios):
    def __init__(self, cvv="", ano_expiracion="", mes_expiracion="", 
                 fecha_expiracion=date.today(), numero=1234567890, zip_codigo=12345,
                 empresa="", valor="", descripcion=""):
        self._cvv = cvv
        self._ano_expiracion = ano_expiracion
        self._mes_expiracion = mes_expiracion
        self._fecha_expiracion = fecha_expiracion
        self._numero = numero
        self._zip_codigo = zip_codigo
        self.empresa = empresa
        self.valor = valor
        self.descripcion = descripcion

    def realizar_servicio_targeta(self):
        print("Agendando tarjeta")
        self.empresa = input("Empresa: ")
        self.valor= input("Valor: ")
        self.descripcion = input("Descripcion: ")
        self._cvv = input("Ingrese el CVV: ")
        self._ano_expiracion = input("Ingrese el año de expiración: ")
        self._mes_expiracion = input("Ingrese el mes de expiración: ")
        self._fecha_expiracion = input("Ingrese la fecha de expiración (dd/mm/yy): ")
        self._numero = input("Ingrese el número: ")
        self._zip_codigo = input("Ingrese el código ZIP: ")
        print("Tarjeta agendada")
    def realizar_servicio_programa(self):
        pass
    def realizar_servicio_seguro(self):
        pass
    def imprimir_servicio_targeta(self):
        return (
            f"CVV: {self._cvv}\n"
            f"Año de expiración: {self._ano_expiracion}\n"
            f"Mes de expiración: {self._mes_expiracion}\n"
            f"Fecha de expiración: {self._fecha_expiracion}\n"
            f"Número: {self._numero}\n"
            f"Código ZIP: {self._zip_codigo}\n"
            f"Empresa: {self.empresa}\n"
            f"Valor: {self.valor}\n"
            f"Descripción: {self.descripcion}\n"
        )
    def imprimir_servicio_programa(self):
        pass
    def imprimir_servicio_seguro(self):
        pass
    
    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, value):
        self._cvv = value

    @property
    def ano_expiracion(self):
        return self._ano_expiracion

    @ano_expiracion.setter
    def ano_expiracion(self, value):
        self._ano_expiracion = value

    @property
    def mes_expiracion(self):
        return self._mes_expiracion

    @mes_expiracion.setter
    def mes_expiracion(self, value):
        self._mes_expiracion = value

    @property
    def fecha_expiracion(self):
        return self._fecha_expiracion

    @fecha_expiracion.setter
    def fecha_expiracion(self, value):
        self._fecha_expiracion = value

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def zip_codigo(self):
        return self._zip_codigo

    @zip_codigo.setter
    def zip_codigo(self, value):
        self._zip_codigo = value
    
    @property
    def empresa(self):
        return self._empresa
    @empresa.setter
    def empresa(self, empresa):
        self._empresa = empresa
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, valor):
        self._valor = valor
    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion
    