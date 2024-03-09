from datetime import date

class iservicioprograma 

class Servicioseguro(IGestionServicios):
    def __init__(self,
                tipo_seguro="Sin seguro", numero_poliza="", fecha_inicio=date.today(),
                fecha_vencimiento=date.today(), estado_seguro=False, empresa="", valor="", descripcion=""):

        self.__tipo_seguro = tipo_seguro
        self.__numero_poliza = numero_poliza
        self.__fecha_inicio = fecha_inicio
        self.__fecha_vencimiento = fecha_vencimiento
        self.__estado_seguro = estado_seguro
        self.__empresa = empresa
        self.__valor = valor
        self.__descripcion = descripcion
    
    def realizar_servicio_targeta(self):
        pass
    def realizar_servicio_programa(self):
        pass
    def realizar_servicio_seguro(self):
        print("Agendando seguro")
        self.__empresa = input("Empresa: ")
        self.__valor = input("Valor: ")
        self.__descripcion = input("Descripcion: ")
        self.__tipo_seguro = input("Ingrese el tipo de seguro: ")
        self.__numero_poliza = input("Ingrese el numero de poliza: ")
        self.__fecha_inicio = input("Ingrese la fecha de inicio (dd/mm/yy): ")
        self.__fecha_vencimiento = input("Ingrese la fecha de vencimiento (dd/mm/yy): ")
        self.__estado_seguro = input("Ingrese el estado del seguro: ")
        return "Seguro agendado"
    def imprimir_servicio_targeta(self):
        pass
    def imprimir_servicio_programa(self):
        pass
    def imprimir_servicio_seguro(self):
        return (
            f"\n"
            f"\tTipo de seguro: {self.__tipo_seguro}\n"
            f"\tNumero de poliza: {self.__numero_poliza}\n"
            f"\tFecha de inicio: {self.__fecha_inicio}\n"
            f"\tFecha de vencimiento: {self.__fecha_vencimiento}\n"
            f"\tEstado del seguro: {self.__estado_seguro}\n"
            f"\tEmpresa: {self.__empresa}\n"
            f"\tValor: {self.__valor}\n"
            f"\tDescripcion: {self.__descripcion}\n"
        )

    @property
    def tipo_seguro(self):
        return self.__tipo_seguro
    @tipo_seguro.setter
    def tipo_seguro(self, tipo_seguro):
        self.__tipo_seguro = tipo_seguro

    @property
    def numero_poliza(self):
        return self.__numero_poliza
    @numero_poliza.setter
    def numero_poliza(self, numero_poliza):
        self.__numero_poliza = numero_poliza

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento
    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha_vencimiento):
        self.__fecha_vencimiento = fecha_vencimiento

    @property
    def estado_seguro(self):
        return self.__estado_seguro
    @estado_seguro.setter
    def estado_seguro(self, estado_seguro):
        self.__estado_seguro = estado_seguro

    @property
    def empresa(self):
        return self.__empresa
    @empresa.setter
    def empresa(self, empresa):
        self.__empresa = empresa

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion
