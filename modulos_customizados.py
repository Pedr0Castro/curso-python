"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então todos os programas ou todos os arquivos que criamos
nesse cursos são módulos Python prontos para serem utilizados

# Importando uma função específica do nosso módulo

from funcoe_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# Importando todo o módulo ( Temos acesso a todos elementos do módulo)
import funcoe_com_parametro as fcp

# Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))
"""

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
