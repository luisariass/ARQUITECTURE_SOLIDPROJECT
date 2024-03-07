from Recomendaciones import Recomendaciones
from Usuarios import Usuarios
from Ubicacion import Ubicacion
from GestionServicios import GestionServicios
from App import App

app = App()


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

    {1: view_profile, 2: admin_ubicacion, 3:admin_interes, 4:admin_beneficios}[op](user)

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
        return admin_ubicacion(user)

    elif op == 2:
        print(user.ubicacio_n)
        return admin_ubicacion(user)

    elif op == 3:
        return menu_comprador()

def admin_interes(user):
    print("Administrar Intereses")
    print("1. Modificar Intereses")
    print("2. Ver Intereses")
    print("3. Salir")

    op = int(input())

    while op not in range(1, 4):
        print("Invalid option")
        op = int(input())

    if op == 1:
        print("Modificar Intereses")
        interes = input("Interes: ")
        user.recomendacione_s = Recomendaciones(interes)
        return admin_interes(user)
    elif op == 2:
        print(user.recomendacione_s)
        return admin_interes(user)

    elif op == 3:
        return menu_comprador()

def admin_beneficios(user):
    print("Administrar Beneficios")
    print("1. Agendar Servicios")
    print("2. Mis Servicios")
    print("2. Salir")
    op = int(input())
    while op not in range(1, 3):
        print("Invalid option")
        op = int(input())
    if op == 1:
        print("Que servicio desea agendar?")
        print("1. Seguro")
        print("2. Tarjeta")
        print("3. Programa de fidelizacion")
        servicio = int(input())

        while servicio not in range(1, 4):
            print("Invalid option")
            servicio = int(input())
        if servicio == 1:
            print("Agendar Seguro")
            empresa_proveedora = input("Empresa proveedora: ")
            valor_servicio = int(input("Valor del servicio: "))
            descripcion_servicio = input("Descripcion del servicio: ")
            user.servicio_s = GestionServicios(empresa_proveedora, valor_servicio, descripcion_servicio)
        if servicio == 2:
            print("Agendar Tarjeta")
            cvv = input("CVV: ")
            ano_expiracion = input("Año de expiracion: ")
            mes_expiracion = input("Mes de expiracion: ")
            fecha_expiracion = input("Fecha de expiracion (dd/mm/yy): ")
            numero = int(input("Numero: "))
            zip_codigo = int(input("Codigo ZIP: "))
            user.servicio_t = GestionServicios(cvv, ano_expiracion, mes_expiracion, fecha_expiracion, numero, zip_codigo)
        if servicio == 3:
            print("Agendar Programa de fidelizacion")
            nombre_programa = input("Nombre del programa: ")
            tipo_programa = input("Tipo de programa: ")
            fecha_inicio = input("Fecha de inicio (dd/mm/yy): ")
            user.servicio_p = GestionServicios(nombre_programa, tipo_programa, fecha_inicio)
    if op == 2:
        print("Mis Servicios")
        print("1. Seguro")
        print(user.servicio_s)
        print("2. Tarjeta")
        print(user.servicio_s)
        print("3. Programa de fidelizacion")
        print(user.servicio_s)

    if op == 3:
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
