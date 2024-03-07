#from Usuarios import Usuarios
from Recomendaciones import Recomendaciones
from Usuarios import Usuarios
from Ubicacion import Ubicacion
from App import App

app = App()
#reco = Recomendaciones()


def seleccionar_user():
    id = int(input("Ingrese su id: "))
    user = app.buscar_usuario(id)
    if user is None:
        print("Usuario no encontrado")
        return
    return user

def menu_comprador():
    user = seleccionar_user()
    if user is None:
        return
    print("")
    print("Bienvenido a la aplicacion señor usuario")
    print("1. Ver perfil")
    print("2. Administrar Ubicacion")
    print("3. Administrar Intereses")
    print("4. Administrar Beneficios")
    print("5. Salir")
    print("")

    op = int(input())

    while op not in range(1, 6):
        print("Invalid option")
        op = int(input())

    {1: view_profile, 2: admin_ubicacion}[op](user)

def view_profile(user):
    print(user)
    return menu_comprador()

def admin_ubicacion(user):
    print("Administrar Ubicacion")
    print("1. Modificar Ubicacion")
    print("2. Ver Ubicacion")
    print("3. Salir")

    op = int(input())

    while op not in range(1, 4):
        print("Invalid option")
        op = int(input())

    if op == 1:
        print("Modificar Ubicacion")
        direccion = input("Direccion: ")
        ciudad = input("Ciudad: ")
        pais = input("Pais: ")
        user.ubicacio_n= Ubicacion(direccion, ciudad, pais)

    elif op == 2:
        print(user.ubicacio_n)

    elif op == 3:
        return
    
def menu():
    print("Bienvenido a la aplicacion")
    print("1. Registrarse")
    print("2. Iniciar sesion")
    print("3. Salir")

    op = int(input())
    while op not in range(1, 4):
        print("Invalid option")
        op = int(input())

    if op == 1:
        idusuario = int(input("Id: "))
        name = input("Nombre: ")
        email = input("Correo: ")
        contra = input("Contrasena: ")
        fecha_nac = input("Fecha de nacimiento (dd/mm/yy): ")
        gen = input("Genero: ")
        usu = Usuarios(idusuario, name, email, contra, fecha_nac, gen)
        app.registrar_usuario(usu)
        print("\nUsuario registrado con exito\n")

    elif op == 2:
        name = input("Nombre: ")
        contra = input("Contrasena: ")
        if app.inicio_sesion(name, contra):
            menu_comprador()
        else:
            print("Usuario o contrasena incorrectos")

    elif op == 3:
        print("Hasta luego")
        exit()

def main():
    while True:
        menu()

if __name__ == '__main__':
    main()
