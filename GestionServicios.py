from Proveedor import Proveedor
from Servicioseguro import Servicioseguro
from Serviciotargeta import Serviciotargeta
from Servicioprograma import Servicioprograma


class GestionServicios():
    def __init__(self, empresa_proveedora: Proveedor= Proveedor(), valor_servicio: str="", 
                 descripcion_servicio: str="", servicio_s: Servicioseguro=Servicioseguro(), 
                 servicio_t:Serviciotargeta=Serviciotargeta(), servicio_p:Servicioprograma=Servicioprograma()):
        
        self.__empresa_proveedora = empresa_proveedora
        self.__valor_servicio = valor_servicio
        self.__descripcion_servicio = descripcion_servicio
        self.__servicio_s = servicio_s
        self.__servicio_t = servicio_t
        self.__servicio_p = servicio_p
        #self.__servicios = []
    
    def __str__(self):
        return (
            f"Proveedor: {self.__empresa_proveedora}\n"
            f"Valor del servicio: {self.__valor_servicio}\n"
            f"Descripcion del servicio: {self.__descripcion_servicio}\n"
            f"Servicio de seguros: {self.__servicio_s}\n"
            f"Servicio de targeta: {self.__servicio_t}\n"
            f"Servicio de programa: {self.__servicio_p}\n"
        )

    @property
    def empresa_proveedora(self):
        return self.__empresa_proveedora

    @empresa_proveedora.setter
    def empresa_proveedora(self, value):
        self.__empresa_proveedora = value

    @property
    def valor_servicio(self):
        return self.__valor_servicio

    @valor_servicio.setter
    def valor_servicio(self, value):
        self.__valor_servicio = value

    @property
    def descripcion_servicio(self):
        return self.__descripcion_servicio

    @descripcion_servicio.setter
    def descripcion_servicio(self, value):
        self.__descripcion_servicio = value

    @property
    def servicio_s(self):
        return self.__servicio_s

    @servicio_s.setter
    def servicio_s(self, value:Servicioseguro):
        self.__servicio_s = value

    @property
    def servicio_t(self):
        return self.__servicio_t

    @servicio_t.setter
    def servicio_t(self, value:Serviciotargeta):
        self.__servicio_t = value

    @property
    def servicio_p(self):
        return self.__servicio_p

    @servicio_p.setter
    def servicio_p(self, value:Servicioprograma):
        self.__servicio_p = value