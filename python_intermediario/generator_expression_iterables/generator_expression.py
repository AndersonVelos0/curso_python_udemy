


# É utilizado para 
import sys

# Generator não tem tamanho, não tem indice, nao tem nada disso
# Generator só existe no python
# Generator são funções que sabem pausar quando necessário, ele executa de novo quando você pedir
# Todo generator é um iterator, mas um iterator não é um generator

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
# a lista está salvando todos os valores na memória
lista = [n for n in range(1000000)]

# criando um generator quando você não quer carregar todos esses dados na memória, apenas um por vez
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)

for n in generator:
    print(n)
