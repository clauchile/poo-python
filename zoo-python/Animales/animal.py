class Beast:
    def __init__(self, name, edad,salud, nivelDeFelicidad):
        self.name = name
        self.edad = edad
        self.salud = salud
        self.nivelDeFelicidad = nivelDeFelicidad
    
    def mostrarInfo(self):
                    
        print("-"*100)
        # if type(self).__name__ == "Tigre":
                # print(f'el animal \'{self.name}\' tiene {self.salud} de salud  y {self.nivelDeFelicidad} de felicidad, su peso es {self.peso} Kg. y es de clase \'{type(self).__name__}\'')
        print(f'\'{self.name}\' es un \'{type(self).__name__}\' tiene {self.salud} de salud  y {self.nivelDeFelicidad} de felicidad')
        return self

    def alimentar(self)->str:
        raise NotImplementedError
        # if name:
        #     for animal in self.animals:
        #         if animal.name == name:
        #             pass
                    # animal.mostrarInfo()
        # else:
        #     for animal in self.animals:
        #         animal.mostrarInfo()
        # """ Cada animal tiene su propia cantidad de salud
        # y de felicidad al alimentarlo"""
        # if type(self).__name__ == "Tigre":
        #     self.salud += 30
        #     health = 30
        #     self.nivelDeFelicidad += 50
        #     happiness = 50
        # elif type(self).__name__ == "Oso":
        #     self.salud += 20
        #     health = 20
        #     self.nivelDeFelicidad += 40
        #     happiness = 40
        # elif type(self).__name__ == "Leon":
        #     self.salud += 50
        #     health = 50
        #     self.nivelDeFelicidad += 40
        #     happiness = 40
        # else: self.salud += 40
        # health = 40
        # self.nivelDeFelicidad += 45
        # happiness = 45
        # print("-"*50)
        # print(f'Se ha aumentado exitosamente {health} de salud y {happiness} de felicidad')
        # return self 

    # def diferenteAlimento(self):

        
