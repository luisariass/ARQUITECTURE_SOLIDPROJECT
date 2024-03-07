from abc import ABC, abstractmethod

class IProveedor(ABC):
    @abstractmethod
    def registrar(self, proveedor):
        pass

    @abstractmethod
    def consultar(self, idprov):
        pass

    @abstractmethod
    def consultarTodos(self):
        pass

    @abstractmethod
    def modificar(self, proveedor):
        pass

    @abstractmethod
    def eliminar(self, idprov):
        pass

class Proveedor: 
    def __init__(self, idprov=None, nombre=None, tipo=None, telefono=None, email=None):
        self.proveedores = [
            {'idprov': 1, 'nombre': 'BANCOLOMBIA', 'tipo': 'BANCARIA', 'telefono': '1234567890', 'email': 'bancolombia@email.com'},
            {'idprov': 2, 'nombre': 'SURA', 'tipo': 'ASEGURADORA', 'telefono': '0987654321', 'email': 'sura.com'},
            {'idprov': 3, 'nombre': 'EXITO 3', 'tipo': 'PROGRAMA ', 'telefono': '1122334455', 'email': 'exito@email.com'},
        ]
        if idprov and nombre and tipo and telefono and email:
            self.proveedores.append({'idprov': idprov, 'nombre': nombre, 'tipo': tipo, 'telefono': telefono, 'email': email})

    def __str__(self):
        return (
            f"Email: {self.email}\n"
            f"Nombre: {self.nombre}\n"
            f"Dirección: {self.direccion}\n"
            f"Teléfono: {self.telefono}\n"
        )

    def consultar(self, idprov):
        for proveedor in self.proveedores:
            if proveedor['idprov'] == idprov:
                return proveedor