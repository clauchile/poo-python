if __name__ == '__main__':
    from animal import *
else:
    from .animal import *
class Leon(Beast):
    def __init__(self, name,edad,salud = 120, nivelDeFelicidad=180):
        super().__init__(name,edad,salud,nivelDeFelicidad)
        
    def alimentar(self):
            if type(self).__name__ == "Leon":
                self.salud += 30
                health = 30
                self.nivelDeFelicidad += 50
                happiness = 50
                print(f'Se ha alimentado exitosamente a \'{self.name}\', ahora posee {health} mas de salud y {happiness} mas de felicidad')
                return self 

if __name__ == "__main__":
    leo = Leon("Leonero",2,130)

    print(leo.name)