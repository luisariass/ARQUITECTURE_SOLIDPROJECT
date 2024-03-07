from Usuarios import Usuarios
from Ubicacion import Ubicacion
from Recomendaciones import Recomendaciones
from GestionServicios import GestionServicios

class Comprador(Usuarios):
    def __init__(self, id, nombre, correo, contasena, fecha_naciemiento, genero, ubicacion:Ubicacion=Ubicacion(), recomendaciones:Recomendaciones=Recomendaciones(), gestionservicios:GestionServicios=GestionServicios()):
        super().__init__(id, nombre, correo, contasena, fecha_naciemiento, genero)
        self.ubicacion = ubicacion  # Crear una instancia de Ubicacion
        self.intereses = recomendaciones  # Crear una instancia de Recomendaciones
        self.beneficios = gestionservicios # Crear una instancia de GestionServicios
    
    def get_ubicacion(self):
        return self.ubicacion
    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion
    def get_intereses(self):
        return self.intereses
    def set_intereses(self, intereses):
        self.intereses = intereses
    def get_beneficios(self):
        return self.beneficios
    def set_beneficios(self, beneficios):
        self.beneficios = beneficios

    def __str__(self):
        return (
            f"Comprador:\n"
            f"{super().__str__()}"
            f"Ubicacion: {self.ubicacion}\n"
            f"Intereses: {self.intereses}\n"
            f"Beneficios: {self.beneficios}\n"
        )
