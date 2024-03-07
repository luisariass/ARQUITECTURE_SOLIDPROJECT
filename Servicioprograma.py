from datetime import date

class Servicioprograma():
    def __init__(self, nombre_programa="Programa predeterminado", tipo_programa="Tipo predeterminado", 
                 fecha_inicio=date.today()):
        
        self.nombre_programa = nombre_programa
        self.tipo_programa = tipo_programa
        self.fecha_inicio = fecha_inicio

    def __str__(self):
        return(
            f"Nombre del programa: {self.nombre_programa}\n"
            f"Tipo de programa: {self.tipo_programa}\n"
            f"Fecha de inicio: {self.fecha_inicio}\n"
        )
    
    @property
    def nombre_programa(self):
        return self.__nombre_programa
    @nombre_programa.setter
    def nombre_programa(self, nombre_programa):
        self.__nombre_programa = nombre_programa
    @property
    def tipo_programa(self):
        return self.__tipo_programa
    @tipo_programa.setter
    def tipo_programa(self, tipo_programa):
        self.__tipo_programa = tipo_programa
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio