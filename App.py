class App:
    # access_log: dict[str, dict[str, int]] = {}
    def __init__(self):
        self.__usuarios = []

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def inicio_sesion(self, nombre_usuario, contrasena):
        for usuario in self.__usuarios:
            if usuario.nombre == nombre_usuario and usuario.contrasena == contrasena:
                return True
        return False

    def buscar_usuario(self, user_id):
        for usuario in self.__usuarios:
            if usuario.idusuario == user_id:
                return usuario
        return None

    @property
    def usuarios(self):
        return self.__usuarios
