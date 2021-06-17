from typing import Union


class Usuario:
    def __init__(self,name,apellido):
        self.name = name
        self.apellido = apellido
        self.account_balance = 0

    def __str__(self):
            return f"El nombre del Usario es: {self.name}"

    def make_deposit(self, amount:Union[int]):
        """Recibe un monto y lo suma al valor de la cuenta"""
        self.account_balance += amount

    def make_withdrawal(self, amount:Union[int]):
        """Descuenta de la cuenta el valor asignado"""
        self.account_balance-=amount

    def display_user_balance(self):
        return f'Usuario: {self.name} {self.apellido}, Saldo {self.account_balance}'
    
    # def transfer_money(self, other_usuario, amount):
    #     other_usuario.make_deposit = other_usuario.account_balance +=amount
    def transfer(self, usuario_destino, monto):
        if self.account_balance < monto:
            print(f"NO TIENE SALDO SUFIENTE {self.nombre}- SALDO: {self.account_balance} falta: { monto - self.account_balance } ")
            return self

        self.make_withdrawal(monto)
        usuario_destino.make_deposit(monto)
        print(f"{self.name} {self.apellido} transfirio a {usuario_destino.name} { usuario_destino.apellido} un total de {monto} los nuevos saldos son:\n{self.display_user_balance()}\ny {usuario_destino.display_user_balance()}")
        # y \n {usuario_destino.name} posee {usuario_destino.account_balance()}")

        return self





# instancia1
UsuarioOne= Usuario("Claudio","Bravo")

UsuarioOne.make_deposit(500)
UsuarioOne.make_deposit(5000)
UsuarioOne.make_deposit(3300)
UsuarioOne.make_withdrawal(2000)
print(UsuarioOne.display_user_balance())

#Instancia2
UsuarioTwo= Usuario("Charles","Aranguiz")
UsuarioTwo.make_deposit(5900)
UsuarioTwo.make_deposit(5000)
UsuarioTwo.make_withdrawal(2000)
UsuarioTwo.make_withdrawal(2780)
print(UsuarioTwo.display_user_balance())

#Instancia3
UsuarioThree= Usuario("Eugenio","Mena")
UsuarioThree.make_deposit(15200)
UsuarioThree.make_withdrawal(2000)
UsuarioThree.make_withdrawal(1780)
UsuarioThree.make_withdrawal(2780)
print(UsuarioThree.display_user_balance())


UsuarioOne.transfer(UsuarioThree,5000)
# print(UsuarioOne.display_user_balance())
# print(UsuarioThree.display_user_balance())
UsuarioTwo.transfer(UsuarioOne,2000)
