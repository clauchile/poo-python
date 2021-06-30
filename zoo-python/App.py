from zoo import *
from colorama import init
from colorama import Fore, Back, Style
init()

# print(Back.RED + Fore.GREEN + "Recursos Python")

print(Fore.GREEN+"="*45+"Bienvenido a ZooMaker"+"="*45)

while True:
    resp = int(input("¿Qué desea hacer?\n1-Comenzar a Jugar\n2-Salir\n¿Cuál es su opción?: "))
    print(Fore.GREEN+"="*100)
    if resp == 1:
        x = input("Para empezar escriba el nombre para su zoologico: ")
        x= Zoo(x)
        break
    elif resp ==2 :
        break    
    # break
    else: 
        print("="*100)
        print(Style.BRIGHT+Fore.RED + "Debe elegir entre 1 y 5")
        print("="*100)
    # print("="*100)
# print(f'el nombre del Zoologico es {x.zooName}')
    # break
while True:
    print(Fore.BLUE+"="*100)
    choice = int(input(f"¿Qué desea hacer?\n1-Agregar animal\n2-Alimentar animal\n3-Mostrar animal\n4-Mostrar todos los animales\n5-Salir\nElija una acción: "))
    # break
    if choice==1:
        """Agregar animal"""
        print(Fore.LIGHTYELLOW_EX+"="*100)
        animal=int(input(f"Elija el tipo de animal\n1- Oso\n2- León\n3- Tigre\nSu elección es: "))
        if animal ==1:
            animal = Oso
        elif animal==2:
            animal=Leon
        elif animal==3:
            animal=Tigre

        nombreDelAnimal =input("¿Cuál es el nombre?: ")
        edadDelAnimal = int(input("¿Cuál es la edad?: "))

        x.agregar_animal(animal,nombreDelAnimal,edadDelAnimal)
        x.mostrar_animales(nombreDelAnimal)

    elif choice ==2:
        print(Fore.LIGHTMAGENTA_EX +"="*100)
        elegir = int(input("Elija una alternativa\n1-Alimentar a todos\n2-Alimentar a un animal escogido\n"))
        if elegir ==1:
            for animal in x.animals:
                animal.alimentar()
            print("="*100)
        elif elegir ==2:
            print("="*100)
            i = 0
            for animal in x.animals:
                i+=1
                print(f'{i}-{animal.name}')
            ele=int(input("¿Qué animal desea alimentar?\n "))
            # print(i)
            x.animals[ele-1].alimentar()
            print("="*100)
        # break


        # break
        
    elif choice ==3:
        print("="*100)
        nombreDelAnimal =input("¿Cuál es el nombre del animal que desea ver la info?: ")
        x.mostrar_animales(nombreDelAnimal)
        
    elif choice ==4:
        print("="*100)
        # nombreDelAnimal =input("¿Cuál es el nombre del animal que desea ver la info?: ")
        x.mostrar_animales()
    elif choice == 5:
        break
    else: 
        print("="*100)
        print(Style.BRIGHT+Fore.RED + "Debe elegir entre 1 y 5")
        



