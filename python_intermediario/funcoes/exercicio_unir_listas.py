# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# Biblioteca para importar o zip_longest
from itertools import zip_longest

# Função para unir duas listas 

def zipper (lista1, lista2):
    intervalo = min(len(lista1), len(lista2))   
    # Convertendo em tupla para e mostrando o indice com o i
    return [(lista1[i], lista2[i]) for i in range(intervalo)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(zipper(l1, l2))

# Contudo, o python já possui funções prontas para fazer essas tarefas
# A função zip no python retorna um iterator, sendo necessário consumi-lo com um for ou transformar em list
# Une a menor lista na lista maior
print(list(zip(l1,l2)))

# O python também tem o zip_longest para utilizar o valor da maior lista e unir a menor
print(list(zip_longest(l1,l2)))
