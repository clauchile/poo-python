class product:
    def __init__(self,codigoP: int,nombreP: str,precioP: int,categoriaP: str):
        self.nombreP = nombreP
        self.precioP = precioP
        self.categoriaP =categoriaP
        self.codigoP = codigoP

    # def __str__(self):
    #     info = f"El producto es \"{self.nombreP}\", su precio es \"{self.precioP}\", y su categoría es \"{self.categoriaP}\""
    #     return info

#actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje de cambio proporcionado. 
# Si es False, el precio debe disminuir en el cambio porcentual proporcionado.
    def actualiza_precio(self, porcentaje_de_incremento:float, incremento:bool =True): 
        """incrementa si es 'True' o disminuye si es 'False' en el porcentaje dado 
        el valor del producto"""
        if incremento:
            self.precioP = self.precioP + (self.precioP * porcentaje_de_incremento)
        else:
            self.precioP = self.precioP - (self.precioP * porcentaje_de_incremento)

    def info_producto(self)->str:
        """Devuelve la informacion del producto"""
        print(f"El producto \"{self.nombreP}\", su precio es \"{self.precioP}\", y su categoría es \"{self.categoriaP}\"")
        return self

        
if __name__ == "__main__":
    P2 = product("Pera",5,"Frutas")
    P2.actualiza_precio(0.02,False)
    # print(P2)
    # print(P2.info_producto())
    P2.info_producto()

    # P2.inflacion(0.09)
    # print(P2)

    