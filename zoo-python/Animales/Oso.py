if __name__ == '__main__':
    from animal import *
else:
    from .animal import *
class Oso(Beast):
    def __init__(self,name,edad,salud=150, nivelDeFelicidad = 120):
        super().__init__(name,edad,salud,nivelDeFelicidad)

    def alimentar(self):
        if type(self).__name__ == "Oso":
            self.salud += 20
            health = 20
            self.nivelDeFelicidad += 40
            happiness = 40
            print(f'Se ha alimentado exitosamente a \'{self.name}\', ahora posee {health} mas de salud y {happiness} mas de felicidad')
            return self

if __name__ == "__main__":
    oso1 = Oso("Apest_oso",5)

    print(oso1.name)
