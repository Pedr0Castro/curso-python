"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita, da mesma forma, se abrirmos um arquivo para
a escrita, não podemos ler, apenas escrever.

# OBS: AO abrir um arquivo para escrita, o arquivo é criado no sistema operacional

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write()
Esta função recebe uma string como parametro.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir, será criado, caso ele já exista
o anterior será apagado e um novo será criado. Dessa forma, todo o conteúdo no arquivo anterior é perdido

# Exemplo de escrita

# FORMA TRADICIONAL DE ESCRITA (NÃO PYTHONICA)
arquivo = open('mais.txt', w', encoding='utf-8')

arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto')

arquivo.close()

# Forma Pythonica
with open('novo.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Novos dados.\n')
    arquivo.write('Outros .\n')
    arquivo.write('Mais Esta é a ultima linha.')

with open('geek.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Geek ' * 1000)


"""
with open('frutas.txt', 'w', encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
