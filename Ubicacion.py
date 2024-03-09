class Ubicacion():
    def __init__(self, direccion: str ="Sin asignar", ciudad: str = "Sin asignar", 
                 pais: str = "Sin asignar"):
        
        self.__direccion = direccion
        self.__ciudad = ciudad
        self.__pais = pais
    
    def __str__(self):
        return (
            f"\n"
            f"\tDireccion: {self.__direccion}\n"
            f"\tCiudad: {self.__ciudad}\n"
            f"\tPais: {self.__pais}\n"
        )
        

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion:str):
        self.__direccion = direccion
    @property
    def ciudad(self):
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, ciudad:str):
        self.__ciudad = ciudad
    @property
    def pais(self):
        return self.__pais
    @pais.setter
    def pais(self, pais:str):
        self.__pais = pais
    