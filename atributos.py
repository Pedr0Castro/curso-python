"""
POO - Atributos

Atributos -Representam as caracteristicas do objeto, ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto.


Em Python, dividimos os atributos em tres grupos:
- atributos de instancia:
- atributos de classe;
- atributos dinamicos;

# Atributos de instancia: São atributos declarados dentro do método construtor

# OBS: Método construtor é um método especial utilizado para a construção do objeto


# Em Java, uma classe Lampada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

    pulic int get
}

Em Python, por convenção ficou estabelecido que todo atributo de uma classe é publico.
Caso queira demonstrar que determinado atributo deve ser tratado como privado, utiliza-se __ duplo underscore
no inicio de seu nome.

Isso é conhecido também como Name Mangling

# OBS: Isso é apenas por convenção , ou seja, a linguagem Python não vai impedir que façamos
# acesso aos atributos sinalizados como privados fora da classe

# exemplos


user = Acesso('user@gmail.com', '123456')

print(user.email)

print(user._Acesso__senha)  # Temos acesso, mas não deveriamos fazer este acesso.

# Atributos de instancia

# significa que ao criarmos instancias de uma classe, todas as instancias
# terão estes atributos.

user1 = Acesso('user1@gmail.com', '1122324')
user2 = Acesso('user2@gmai.com', '12232432')

user1.mostra_email()
user2.mostra_email()

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)  # Acesso possível mas incorreto
print(p2.valor)  # # Acesso possível mas incorreto

# OBS : não precisamos criar uma instancia de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos de classe aqui no Python são chamados de atributos estáticos;
"""

# Classes com atributos de instancia públicos

class Lampada:

    def __int__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __int__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __int__(self,nome ,email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos publicos e atributos privados

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos dinamicos - Um atributo de instancia que pode ser criado em tempo de execução

# OBS: o atributo dinamico será exclusivo da instancia que o criou.

p1 = Produto('Playstation 4', 'Video Game', 2300)

p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinamico em tempo de execução

p2.peso = '5kg'

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso {p2.peso}')

# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso {p1.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

# print(Produto.__dict__)

del p2.peso
del p2.valor

print(p1.__dict__)
print(p2.__dict__)