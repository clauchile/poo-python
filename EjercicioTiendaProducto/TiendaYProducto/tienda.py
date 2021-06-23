# import producto
class Tienda:
    def __init__(self,nombre:str):
        """Constructor de una tienda"""
        self.nombre = nombre
        self.productos = []
    
    def __str__(self):
        lista = []
        # print(self.nombre)
        
        for producto in self.productos:
            lista.append(producto)
        if not lista:
            dr = (f'el nombre de la tienda es: {self.nombre} y aun no tiene productos')
        else:
            dr = (f'el nombre de la tienda es: {self.nombre} y los productos son: {self.productos}')

        return dr

        #add_product (self, new_product) : toma un producto y lo agrega a la tienda
    def agrega_producto(self, Nproducto:str)->str:
        """Agrega un nuevo producto. Debe ser("nuevo producto")"""
        # self.Nproducto = Nproducto
        print("="*30 + "NUEVO PRODUCTO" + "="*70)
        self.productos.append(Nproducto)
        print(f'\'{Nproducto.nombreP}\' fue agregado exitosamente su valor es \'{Nproducto.precioP}\'')
        return self

    def venta_producto(self, cod:int)->str:
        print("="*30 + "VENTA" + "=" * 70)
        id = -1
        for producto in self.productos:
            id+=1
            if producto.codigoP == cod:
                break
        producto = self.productos.pop(id)
        # ret = self.productos.pop(id)
        print(f"el producto vendido es '{producto.nombreP}' y su codigo es {cod}")
        # print("="*100)
        return self


    def mostrar_productos(self):         
        for p in self.productos:
            p.info_producto()

    def inflacion(self, porcentaje_de_variacion): 
        print("="*30 + "INFLACION" + "="*70)
        for pr in self.productos:
            pr.actualiza_precio(porcentaje_de_variacion,True)
            
            print(f'el valor de \'{pr.nombreP}\' se ha incrementado en \'{(porcentaje_de_variacion)*100}%\', ahora su valor es {pr.precioP}')
        # print("="*100)
        return self

    def set_clearance(self, categoria, porcentaje): 
        print("="*30 + "BAJA EN EL PRECIO" +"="* 70)
        for p in self.productos:
            if p.categoriaP == categoria:
                p.actualiza_precio(porcentaje,False)
        print(f"Se ha actualizado el valor de la categoria '{categoria}' en -{(porcentaje)*100}%")
        
        

if __name__ == "__main__":
    T1=Tienda("Tiendita1")
    T1.productos=["Manzanas", "Peras"]
    T1.agrega_producto("Mangos")
    T1.agrega_producto("Ciruelas")
    print(T1)
    T1.venta_producto("Peras")
    # T1.


    T1.info_producto()
