
class BankAccount:
    def __init__(self, name, apellido, tasa_interes= 0.01, balance=0): # ¡No olvides agregar valores predeterminados para estos parámetros!
		# su código aquí! (recuerde, aquí es donde especificamos los atributos para nuestra clase)
                # no se preocupe por la información del usuario aquí; pronto involucraremos a la clase de usuario
        self.name = name
        self.apellido = apellido
        self.balance = balance
        self.tasa_interes= tasa_interes

#La clase también debe tener los siguientes métodos:

# deposit(self, cantidad) : aumenta el saldo de la cuenta en la cantidad dada
# withdraw(self, cantidad) : disminuye el saldo de la cuenta en la cantidad dada 
# si hay fondos suficientes; si no hay suficiente dinero, imprima un mensaje 
# "Fondos insuficientes: cobrar una tarifa de $ 5" y deduzca $ 5
# display_account_info(self) - imprime en la consola: ej. "Saldo: $ 100"
# yield_interest(self) : aumenta el saldo de la cuenta en el saldo actual * la tasa de interés 
# (siempre que el saldo sea positivo)
# Esto significa que necesitamos una clase que se vea así:
                
    def deposito(self, amount):
        self.balance += amount
        return self
		# tu código aqui
    def retiro(self, amount):
        if self.balance<amount:
            
            print (f'Fondos insuficientes: el cliente {self.name}, {self.apellido} tiene saldo insuficiente \npor lo que no se puede hacer un retiro por ${amount} \nse cobrara una tarifa de $ 5\nel nuevo saldo es ${self.balance-5}\n')
            return self
        else: self.balance-=amount
        return self
		# tu código aqui
    def saldo_cuenta_info(self):
        print(f'El usuario: {self.name} {self.apellido}, tiene saldo: {round(self.balance)}')
        return self
		# tu código aqui
    def aumenta_interes(self):
        if self.balance>0:
            self.balance = self.balance +(self.balance * self.tasa_interes)
            
        else: print(f'Saldo insuficiente: {self.balance}')
		# tu código aqui
        return self
#cliente1
cliente1=BankAccount("Gracia","Orellana",0.02,5000)
cliente1.deposito(1000).deposito(2000).deposito(3000).retiro(6000).aumenta_interes().saldo_cuenta_info()

#cliente2

cliente2 = BankAccount("Carina", "Tescione",0.03,10000)
cliente2.deposito(1000).deposito(1000).retiro(2000).retiro(2000).retiro(4000).retiro(8000).aumenta_interes().saldo_cuenta_info()