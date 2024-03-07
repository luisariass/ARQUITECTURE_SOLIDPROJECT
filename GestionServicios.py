from Proveedor import Proveedor

class GestionServicios():
    def __init__(self, empresa_proveedora: Proveedor= Proveedor(), valor_servicio: str=" ", descripcion_servicio: str=" "):
        self.empresa_proveedora = empresa_proveedora
        self.valor_servicio = valor_servicio
        self.descripcion_servicio = descripcion_servicio
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def ver_detalles(self):
        return f"Proveedor: {self.empresa_proveedora}, Valor del servicio: {self.valor_servicio}, Descripcion del servicio: {self.descripcion_servicio}"