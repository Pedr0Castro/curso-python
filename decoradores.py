"""
Decoradores (Decorators)

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorator tem uma sintaxe própria, usando @ (Syntact Sugar / açúcar Sintático)

|----------------------------------------------|
|        Function Decorator                    |
------------------------------------------------

-----------------------------------------------
| |-----------------------------------------| |
| |          Função decorada                | |
| |------------------------------------------ |
| --------------------------------------------
# Decorators como funções(Sintaxe não recomendada)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# testando 1

teste = seja_educado(saudacao)

teste()

# Testando 2

def raiva():
    print('EU TE ODEIO')

raiva_educada = seja_educado(raiva)

raiva_educada()

# Decorators com sintaxe sugar


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('meu nome é Pedro')

# testando

apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')

dormir()

|-----------------------------------------------------
|   Home   | serviços    |  Produtos | Administrativo|
------------------------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/serviços

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/admin

# OBS: Não é código funcional, apenas exemplo

def checa_login():
    if not request.usuario:
        redirect('http://www.suaempresa.com.br')

def home(request):
    return 'Pode acessar home'

def serviços(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login
def admin(request):
    return 'Pode acessar admin'

# OBS: Não confuda decorator com decorator function
"""

