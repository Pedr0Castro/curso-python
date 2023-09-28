"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionarios Python são conhecidos como mapas.

Dicionários são coleções do tipo chave/valor

Dicionário são representados por chaves {}

OBS: sobre dicionários
  - chaves e valor são separados por dois pontos 'chave:valor';
  - Tanto chave quanto valor podem ser de qualquer tipo de dado;
  - Podemos misturar os dados;

# Criação de dicionários

# Forma 1 (mais comum)

paises = {'br': 'brasil', 'eua': 'estados unidos', 'py': 'paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

paises = {'br': 'brasil', 'eua': 'estados unidos', 'py': 'paraguai'}

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será
gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('estados unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos Utilizar qualquer tipo de dado inclusive (int, float, string, boolean), inclusive lista, tupla dicionario,
# como chaves de dicionarios.

# Tupla por exemplo são bastante interessantes de serem utilizadas como chaves de dicionário, pois as mesmas
# São imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em SP',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350

print(receita)

# Forma 2
novo_dado = {'mai': 500}

receita.update(novo_dado)  # Receita.update({'mai':500})

print(receita)

# Atualziando dado em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# Conclusão 1 : A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2: Em dicionário, não podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1
ret = receita.pop('mar')
print(ret)

print(receita)

# OBS: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS2: Ao removermos o objeto, o valor desse objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# SE a chave não existir será gerado um KeyError.
# OBS: neste caso o valor removido não é retornado.

# Imagine que você tem um comércio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinho de compras:
     produto 1:
          nome;
          quantidade;
          preço;
     produto 2:
          nome;
          quantidade
          preço;


# Poderiamos utilizar uma lista para isso? sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o indice de cada informação no produto.


# 2 - poderiamos utilizar um tupla para isso

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of war 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o indice de cada informação no produto.

# 3- poderiamos utilizar um dicionário

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# Podemos ter a certeza sobre cada informação.

# Métodos de dicionários.

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)

d.clear()

print(d)

# Copiando um dicionário para outro

# Forma 1 # Deep copy

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método {}.formkeys recebe dois parametros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)
