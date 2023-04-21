"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
# Adicionando com append no ultimo indice da lista
lista.append('Dersinho')
print(lista)
# Removendo
nome = lista.pop() 
print(lista)
# Apagando 
lista.append(1233)
print(lista)
# caso nao saiba o numero de itens na lista, utilizamos menos 1
del lista[-1]
# Limpando a lista com clear
# lista.clear()
print(lista)

# Adicionando com insert, recebe dois parametros, o primeiro é o do indice e o segundo é o item
# Movendo todos os itens a frente
lista.insert(0,5)
print(lista)

# Caso você tente acessar um index que não existe, o seguinte erro irá aparecer:
# IndexError: list index out of range
# print(lista[10])

