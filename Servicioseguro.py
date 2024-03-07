from datetime import date

class Servicioseguro():
    def __init__(self, tipo_seguro="Sin seguro", numero_poliza="", 
                 fecha_inicio=date.today(), fecha_vencimiento=date.today(), estado_seguro=False,):
        self.__tipo_seguro = tipo_seguro
        self.__numero_poliza = numero_poliza
        self.__fecha_inicio = fecha_inicio
        self.__fecha_vencimiento = fecha_vencimiento
        self.__estado_seguro = estado_seguro

    def __str__(self):
        return(
            f"\n"
            f"\tTipo de seguro: {self.__tipo_seguro}\n"
            f"\tNumero de poliza: {self.__numero_poliza}\n"
            f"\tFecha de inicio: {self.__fecha_inicio}\n"
            f"\tFecha de vencimiento: {self.__fecha_vencimiento}\n"
            f"\tEstado del seguro: {self.__estado_seguro}\n"
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
    