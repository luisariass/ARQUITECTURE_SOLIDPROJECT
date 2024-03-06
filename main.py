#from Usuarios import Usuarios
from Comprador import Comprador


def main():
    # Create an instance of Usuarios
    usuario = Comprador(1, "Juan", "a@", "123", "01/01/2000", "M", "mexico", "pintar", 1)
    #usuario = Comprador("mexico", "pintar", 1, "Juan", "a@", "123", "01/01/2000", "M")
    print(usuario)

if __name__ == '__main__':
    main()