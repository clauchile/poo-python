if __name__ == '__main__':
    from animal import *
else:
    from .animal import *

class Tigre(Beast):
    def __init__(self, name,edad,salud=100, nivelDeFelicidad=100):
        super().__init__(name,edad,salud,nivelDeFelicidad)
        self.peso = 400

    def mostrarInfo(self):
        
        print("-"*100)
        # if type(self).__name__ == "Tigre":
        print(f'\'{self.name}\' es un \'{type(self).__name__}\' tiene {self.salud} de salud  y {self.nivelDeFelicidad} de felicidad, y su peso es {self.peso} Kg.')
        # else: print(f'el animal \'{self.name}\' tiene {self.salud} de salud  y {self.nivelDeFelicidad} de felicidad y es de clase \'{type(self).__name__}\'')
        return self
    def alimentar(self):
        if type(self).__name__ == "Tigre":
            self.salud += 30
            health = 30
            self.nivelDeFelicidad += 50
            happiness = 50
            print(f'Se ha alimentado exitosamente a \'{self.name}\', ahora posee {health} mas de salud y {happiness} mas de felicidad')
            return self 
    
if __name__ == "__main__":

    Tigre1 = Tigre("Tiger",5)


    print(Tigre1.peso)
    Tigre1.alimentar()

    Tigre1.mostrarInfo()