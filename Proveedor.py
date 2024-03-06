class Proveedor: 
    def __init__(self, idprov, nombre, tipo, telefono, email):
        self.idprov = idprov
        self.nombre = nombre
        self.tipo = tipo
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f'Nombre: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}, Email: {self.email}'