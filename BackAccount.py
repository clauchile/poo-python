
class BankAccount:
    def __init__(self, int_rate= 0.01, balance=0): # ¡No olvides agregar valores predeterminados para estos parámetros!
		# su código aquí! (recuerde, aquí es donde especificamos los atributos para nuestra clase)
                # no se preocupe por la información del usuario aquí; pronto involucraremos a la clase de usuario
                pass
    def deposit(self, amount):
        self.balance += amount
        return self
		# tu código aqui
    def withdraw(self, amount):
        self.balance-=amount
        return self
		# tu código aqui
    def display_account_info(self):
        print(f'El usuario: {self.name} {self.apellido}, tiene saldo: {self.balance}')
        return self
		# tu código aqui
    def yield_interest(self):
        self.balance = self.balance +(self.balance * self.int_rate)
		# tu código aqui