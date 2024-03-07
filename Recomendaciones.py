class Recomendaciones():
    def __init__(self):
        self.intereses = []
    
    def agregar_interes(self):
        print("Agregar interes: ")
        interes = input("aqui: ")
        intereses = {"intereses": interes} 
        self.intereses.append(intereses)

    def __str__(self):
        return (
            f"\tIntereses: {self.intereses}"
        )