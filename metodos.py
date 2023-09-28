"""
POO - Métodos

- Métodos (funções) - Representam os comportamentos do objeto, ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python dividimos os métodos, em 2 grupos: Métodos de instancia
e Métodos de classe

# Métodos de Instancia

O método dunder init é um método especial chamado de construtor e sua função é
contruir o objeto a partir da classe

# Métodos dunder são chamados métodos mágicos.

p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(5))

user1 = Usuario('Pedro', 'Castro', 'pedro@gmail.com', '12343432')
user2 = Usuario('Junior', 'Castro', 'juniorgmail.com', '12342123432')

print(user1.nome_completo())
print(f'Senha User 1: {user1._Usuario__senha}')
print(f'Senha User 2: {user2._Usuario__senha}')

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirme_senha = input('Confirme a senha: ')

if senha == confirme_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuario criado com sucesso')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso errado

# Métodos de classe

user = Usuario('Pedro', 'Castro', 'pedro@gmail.com', '123456')

Usuario.conta_usuarios()  # FORMA CORRETA
user.conta_usuarios()  # Possivel mas incorreta

user = Usuario('Pedro', 'Castro', 'pedro@gmail.com', '123456')

print(user._Usuario__gera_usuario())
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __int__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Método estático

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Pedro', 'Castro', 'pedro@gmail.com', '123456')

print(user.contador)

print(Usuario.definicao())


