import unittest
# esto es lo que estamos ejecutando nuestra prueba en 
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        sum = 0
        for t in  nums:
            sum +=t
        self.result = self.result+(num+sum)
        # print (num+sum)
        return self
    def subtract(self, num, *nums):
        rest = 0
        for t in  nums:
            rest +=t
        self.result = self.result -(num+rest)
        # print (num+rest)
        return self
    # tu código aquí
# crear una instruccion:
md = MathDojo()

# print(isSuma(2,4,5))
# nuestros "unit tests" 
# inicializado creando una clase que hereda de unittest.TestCase 
class MathDojoPrueba(unittest.TestCase):
    # cada método en esta clase es una prueba que se ejecutará 
    def test1(self):
        self.assertEqual(md.add(2,5,8,9).result,24)

        # otra forma de escribir arriba es 
    def test2(self):
        self.assertEqual(md.add(2,5,8,9).result,24,"Hecho")
    #     self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(md.add(2).subtract(2,3).result,-3)
    #     self.assertEqual(isEven(3), False)
    #     # otra forma de escribir lo de arriba es
    #     self.assertFalse(isEven(3))
    #  cualquier tarea que desee ejecutar antes de ejecutar cualquier método anterior, colóquelas en el método setUp 
    def setUp(self):
        # v= isSuma(2,3)
        md.result = 0
        print("get started")
        # agrega las tareas setUp 
        # print("running setUp"copy)
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método
    def tearDown(self):
        # agrega las tareas tearDown 
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # esto ejecuta nuestras prue