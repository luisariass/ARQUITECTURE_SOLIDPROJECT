class Usuarios():
    def __init__(self, idusuario, nombre, correo, contrasena, fecha_nacimiento, genero):
        self.idusuario = idusuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
    
    def get_idusuario(self):
        return self.idusuario
    def set_idusuario(self, idusuario):
        self.idusuario = idusuario
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nombre):
        self.nombre = nombre
    def get_correo(self):
        return self.correo
    def set_correo(self, correo):
        self.correo = correo
    def get_contrasena(self):
        return self.contrasena
    def set_contrasena(self, contrasena):
        self.contrasena = contrasena
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento
    def get_genero(self):
        return self.genero
    def set_genero(self, genero):
        self.genero = genero

    def __str__(self):
        return (
            f"\tIdusuario: {self.idusuario}\n"
            f"\tNombre: {self.nombre}\n"
            f"\tCorreo: {self.correo}\n"
            f"\tContrasena: {self.contrasena}\n"
            f"\tFecha de nacimiento: {self.fecha_nacimiento}\n"
            f"\tGenero: {self.genero}\n"
        )