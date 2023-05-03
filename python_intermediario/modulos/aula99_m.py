from sys import path

# Formas de importar o módulo 
import testandoModularizacao.modulo
from testandoModularizacao import modulo
from testandoModularizacao.modulo import *

# from aula99_package.modulo import soma_do_modulo

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(testandoModularizacao.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
