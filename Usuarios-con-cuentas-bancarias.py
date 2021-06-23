class User:
    def __init__(self, name, apellido):
        self.name=name
        self.apellido=apellido
        self.cuenta_bancaria=BankAccount(tasa_interes=0.01, balance=0)

    def __str__(self):

        mismo = f"el nombre del cliente es {self.name} {self.apellido}\nsu saldo es: {self.cuenta_bancaria.balance} y su tasa de interes es: {self.cuenta_bancaria.tasa_interes}"
        return mismo



class BankAccount:
    def __init__(self,tasa_interes, balance): # ¡No olvides agregar valores predeterminados para estos parámetros!
		# su código aquí! (recuerde, aquí es donde especificamos los atributos para nuestra clase)
                # no se preocupe por la información del usuario aquí; pronto involucraremos a la clase de usuario
        self.balance = balance
        self.tasa_interes= tasa_interes
        # self.num_cta = num_cta
    def deposito(self, amount):
        
        # self.User.balance += amount
        # self.num_cta = num_cta
        self.balance+= amount
        return self
		# tu código aqui
    def retiro(self,amount):
        if self.balance<amount:
            
            print ("No es posible realizar esta operacion. Fondos insuficientes")
            
        else: self.balance-=amount

        return self
		# tu código aqui
    def saldo_cuenta_info(self):
        print(f'El saldo es: {round(self.balance)}')
        return self
		# tu código aqui
    def aumenta_interes(self):
        if self.balance>0:
            self.balance = self.balance +(self.balance * self.tasa_interes)
            print(f"se ha añadido el interes a su cuenta su nuevo saldo: {self.balance}")
            
        else: print(f'Saldo insuficiente: {self.balance}')
		
        return self

    def transfer(self, usuario_destino:object, monto:int)-> str:
        """Transfiere un monto a otro cliente y devuelve un mensaje si la operacion fue exitosa o no"""
        if self.balance < monto:
            print("No tiene saldo suficiente para realizar  la transaccion")
        else: 
            self.retiro(monto)
            usuario_destino.cuenta_bancaria.deposito(monto)
            print( f"Acabas de transferir a {usuario_destino.name} { usuario_destino.apellido} un total de {monto}, tu nuevo saldo es {self.balance}")
        return self

# SENSEI BONUS: Permite al usuario tener varias cuentas; actualiza los metodos para que el usuario pueda especificar de cual cuenta ellos quieren depositar o retirar
#  BONUS 2: Modificar la función "transfer_money" de la clase User


cliente1 = User("Carina","Tescione")
cliente1.cuenta_bancaria.balance = 1000
cliente1.cuenta_bancaria.tasa_interes = 0.02
# cliente1.cuenta_bancaria =(0.02,1000)
cliente2 = User("Monse", "Contreras")

# print(cliente1)
print(cliente2)

cliente1.cuenta_bancaria.transfer(cliente2,500)
# cliente1.cuenta_bancaria.aumenta_interes()
cliente2.cuenta_bancaria.saldo_cuenta_info()
# cliente2.cuenta_bancaria.transfer()
# print(cliente1.cuenta_bancaria.balance)