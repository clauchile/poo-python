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

x = md.add(2).add(2,5,1).subtract(3).result
print(x)	# debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!

# l =md.subtract(2,1,1).subtract(4,2,1,3).subtract(1,1,1).result
k =md.subtract(1,3,4,5,8).subtract(1,2,5).result
print(k)