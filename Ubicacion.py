class Ubicacion():
    def __init__(self, direccion: str ="predeterminada", ciudad: str = "predetermianda", 
                 pais: str = "predeterminado"):
        
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
        

    def get_direccion(self):
        return self.direccion
    def set_direccion(self, direccion):
        self.direccion = direccion
    def get_ciudad(self):
        return self.ciudad
    def set_ciudad(self, ciudad):
        self.ciudad = ciudad
    def get_pais(self):
        return self.pais
    def set_pais(self, pais):
        self.pais = pais