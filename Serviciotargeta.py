from datetime import date

class Serviciotargeta():
    def __init__(self, cvv="", ano_expiracion="", mes_expiracion="", 
                 fecha_expiracion=date.today(), numero=1234567890, zip_codigo=12345):
        self._cvv = cvv
        self._ano_expiracion = ano_expiracion
        self._mes_expiracion = mes_expiracion
        self._fecha_expiracion = fecha_expiracion
        self._numero = numero
        self._zip_codigo = zip_codigo

    def __str__(self):
        return (
            f"CVV: {self._cvv}\n"
            f"Año de expiración: {self._ano_expiracion}\n"
            f"Mes de expiración: {self._mes_expiracion}\n"
            f"Fecha de expiración: {self._fecha_expiracion}\n"
            f"Número: {self._numero}\n"
            f"Código ZIP: {self._zip_codigo}\n"
        )

    @property
    def cvv(self):
        return self._cvv

    @cvv.setter
    def cvv(self, value):
        self._cvv = value

    @property
    def ano_expiracion(self):
        return self._ano_expiracion

    @ano_expiracion.setter
    def ano_expiracion(self, value):
        self._ano_expiracion = value

    @property
    def mes_expiracion(self):
        return self._mes_expiracion

    @mes_expiracion.setter
    def mes_expiracion(self, value):
        self._mes_expiracion = value

    @property
    def fecha_expiracion(self):
        return self._fecha_expiracion

    @fecha_expiracion.setter
    def fecha_expiracion(self, value):
        self._fecha_expiracion = value

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def zip_codigo(self):
        return self._zip_codigo

    @zip_codigo.setter
    def zip_codigo(self, value):
        self._zip_codigo = value