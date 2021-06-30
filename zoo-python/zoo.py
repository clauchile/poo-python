# from Animales.animal import *
from Animales.Leon import *
from Animales.Oso import *
from Animales.Tigre import *

class Zoo:
    def __init__(self, zooName):
        self.zooName = zooName
        self.animals = []

    def agregar_animal(self, tipo,name,edad):
        self.animals.append(tipo(name, edad))
    
    def mostrar_animales(self,name:str=None)->str:
        ''' Devuelve la info de un animal si se le entrega el nombre como argumento
        o devuelve la información de todos los animales del Zoo sino se le pasa ningúna argumento'''
        print("="*100)
        if name:
            for animal in self.animals:
                if animal.name == name:
                    animal.mostrarInfo()
        else:
            for animal in self.animals:
                animal.mostrarInfo()


if __name__ == "__main__":
    Zoo1 = Zoo("miZoo")
    Zoo1.agregar_animal(Leon,"Mufasa",5)
    Zoo1.agregar_animal(Tigre,"Tiger",8)
    Zoo1.agregar_animal(Oso,"Balu",15)
    # Zoo1.agregar_animal(Iguana,"Ricardo",9)
    Zoo1.animals[1].peso = 500
    
    # Zoo1.mostrar_todos()
    Zoo1.mostrar_animales()

    # print(Zoo1.zooName)
    # # Zoo1.Beast[0].mostrarInfo()
    # Zoo1.animals[0].mostrarInfo()
    # Zoo1.animals[0].alimentar()
    # Zoo1.animals[1].alimentar()
    # Zoo1.animals[0].mostrarInfo()
    # Zoo1.animals[1].mostrarInfo()
    # print(Zoo1.animals[0].edad)
    # # print(Zoo1.animals[1].peso)
    # Zoo1.mostrar_todos()
    Zoo1.mostrar_animales("Tiger")

    

