from Ubicacion import Ubicacion
from Recomendaciones import Recomendaciones
from GestionServicios import GestionServicios

class Usuarios():
    def __init__(self, idusuario:int=0, nombre:str="", correo:str="", 
                 contrasena:str="", fecha_nacimiento:str="", genero:str="", 
                 ubicacio_n:Ubicacion=Ubicacion(), recomendacione_s:Recomendaciones=Recomendaciones(), 
                 servicio_S:GestionServicios=GestionServicios()):
        self.__idusuario = idusuario
        self.__nombre = nombre
        self.__correo = correo
        self.__contrasena = contrasena
        self.__fecha_nacimiento = fecha_nacimiento
        self.__genero = genero
        self.__ubicacio_n = ubicacio_n
        self.__recomendacione_s = recomendacione_s
        self.__servicio_S = servicio_S

    def __str__(self):
        return (
            f"Usuario:\n"
            f"\tIdusuario: {self.__idusuario}\n"
            f"\tNombre: {self.__nombre}\n"
            f"\tCorreo: {self.__correo}\n"
            f"\tContrasena: {self.__contrasena}\n"
            f"\tFecha de nacimiento: {self.__fecha_nacimiento}\n"
            f"\tGenero: {self.__genero}\n"
            f"Ubicacion:{self.__ubicacio_n}"
            f"Intereses: {self.__recomendacione_s}"
            '''
            f"Beneficios seguro: {self.__servicio_S.get_seguros()}"
            f"Beneficios tarjeta: {self.__servicio_S.get_tarjetas()}"
            f"Beneficios programa de fidelizacion: {self.__servicio_S.get_programas()}"
            '''

            
        )
    
    @property
    def idusuario(self):
        return self.__idusuario
    @idusuario.setter
    def idusuario(self, idusuario:int):
        self.__idusuario = idusuario
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre:str):
        self.__nombre = nombre
    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self, correo:str):
        self.__correo = correo
    @property
    def contrasena(self):
        return self.__contrasena
    @contrasena.setter
    def contrasena(self, contrasena:str):
        self.__contrasena = contrasena
    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento:str):
        self.__fecha_nacimiento = fecha_nacimiento
    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, genero:str):
        self.__genero = genero
    @property
    def ubicacio_n(self):
        return self.__ubicacio_n
    @ubicacio_n.setter
    def ubicacio_n(self, ubicacio_n:Ubicacion):
        self.__ubicacio_n = ubicacio_n
    @property
    def recomendacione_s(self):
        return self.__recomendacione_s
    @recomendacione_s.setter
    def recomendacione_s(self, recomendacione_s:Recomendaciones):
        self.__recomendacione_s = recomendacione_s
    @property
    def servicio_S(self):
        return self.__servicio_S
    
    