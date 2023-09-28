"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código, também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe, que passa a herdar
atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Pedro', 'Castro', '153.952.657.71', 500)

funcionario1 = Funcionario('Joelson', 'Aguiar', '123.321.542-01', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

OBS: Quando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra, a classe herdada é conehcida por:
    [Pessoa]
    - super classe;
    - classe mãe;
    - classe pai;
    - classe base;
    - classe genérica
Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - sub classe;
    - classe filha;
    - classe específica;

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum para acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # forma comum de acessar dados
        self.__matricula = matricula


cliente1 = Cliente('Pedro', 'Castro', '153.952.657.71', 5000)

funcionario1 = Funcionario('Joelson', 'Aguiar', '123.321.542-01', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)

# Sobrescrita de Métodos(Overriding)

- Ocorre quando reescrevemos um método presente na super classe em classes filhas
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum para acessar dados da super classe
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # forma comum de acessar dados
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Pedro', 'Castro', '153.952.657.71', 5000)

funcionario1 = Funcionario('Joelson', 'Aguiar', '123.321.542-01', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
