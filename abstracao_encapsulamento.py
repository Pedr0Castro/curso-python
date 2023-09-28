"""
POO - Abstração e Encapsulamento

o grande objetivo da programação orientada a objeto é encapsular nosso código dentro de um grupo lógico e
hierárquico utilizando classes.

# ABstração é o ato de expo apenas dados releevantes de uma classe, escondendo atributos e métodos privados de
usuário.

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)  # Name mangling

conta1._Conta__titular = 'Pedrin'

print(conta1.__dict__)

print(conta1.__dict__)

conta1.depositar(150.0)

print(conta1.__dict__)

conta1.sacar(2000)

print(conta1.__dict__)
"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('salfo insuficiente')
        else:
            print('o valor deve ser positivo')


    def transferir(self, valor, conta_destino):
        # 1 -  remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # taxa de transferencia paga por quem realizou a transferencias

        # 2 - adicionar o valor na conta destino
        conta_destino.__saldo += valor

# testando


conta1 = Conta('pedrin', 150.00, 1500)
conta1.extrato()

conta2 = Conta('joelson', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()
