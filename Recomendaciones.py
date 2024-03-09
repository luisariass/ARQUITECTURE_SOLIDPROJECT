class Recomendaciones:
    def __init__(self, intereses: str = "No tiene intereses"):
        self.__intereses = intereses

    def __str__(self):
        return (
            f"\n"
            f"\t{self.__intereses}\n"
        )

    @property
    def intereses(self):
        return self.__intereses

    @intereses.setter
    def intereses(self, intereses: str):
        self.__intereses = intereses
