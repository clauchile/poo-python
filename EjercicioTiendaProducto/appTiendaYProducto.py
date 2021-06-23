from TiendaYProducto.producto import *
from TiendaYProducto.tienda import *

Market=Tienda("Market")
# Market.productos=["Piñas"]
# Market.agrega_producto("Kiwis")


Pera = product(1,"Peras",600,"Frutas")
Manzana = product(2,"Manzanas",500,"Frutas")
Betarraga = product(3,"Betarragas",700,"Verduras")
Lechuga = product(4,"Lechugas",800,"Verduras")
# print("="*100)

Market.agrega_producto(Pera)
Market.agrega_producto(Manzana)
Market.agrega_producto(Betarraga)
Market.agrega_producto(Lechuga)
# print(Market.mostrar_productos())

Market.inflacion(0.02)

# print("="*100)
Market.venta_producto(1)
# print("="*100)
print(Market.mostrar_productos())

# print("="*100)
Market.set_clearance("Frutas",0.03)
# print("="*100)


print(Market.mostrar_productos())





