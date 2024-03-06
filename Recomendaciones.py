class Recomendaciones():
    def __init__(self):
        self.intereses = []
    
    def agregar_interes(self):
        print("Agregar interes: ")
        interes = input("aqui: ")
        intereses = {"intereses": interes} 
        self.intereses.append(intereses)

    def __str__(self):
        str_intereses = ""
        for interes in self.intereses:
            str_intereses += f"{interes['intereses: ']}\n"
        return str_intereses