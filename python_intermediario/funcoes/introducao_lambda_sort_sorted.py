# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)


# O python não sabe ordenar dicionarios
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# print(lista, type(lista))]


# Criando uma função para ordenar pela chave passada

def ordena(item):
    return item['sobrenome']

# Utilizando a função sort que irá ordenar pela chave passada
# Python utiliza a tabela unicode para ordenar por letras
# Passamos uma função e o python a executa na função de cima
# lista.sort(key = ordena)


def exibe(lista):
    for item in lista: 
        print(item)
    print()
    
    
# Utilizando a função/expressão lambda em uma linha apenas a função é aplicada apenas a listas
# lista.sort(key = lambda item: item['nome'])

# Também é possivel ordenar utilizando a função sorted que funciona com qualquer iteravel
# Retorna uma copia raza da lista
l1 = sorted(lista, key = lambda item: item['nome'])
l2 = sorted(lista, key = lambda item: item['sobrenome'])

# Ambas as listas vão ser exibidas, uma pela chave em ordem do nome e outra pela chave do sobrenome
exibe(l1)
exibe(l2)
