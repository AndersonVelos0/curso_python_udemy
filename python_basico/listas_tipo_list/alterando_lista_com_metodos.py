"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# É interessante trabalhar com lista no final dela, pela necessidade de processamento
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
lista [2] = 300
# Deletando o indice 2 
del lista[2]
print(lista)
print(lista[2])

# Adicionando indices na ponta no final da lista
# O método pop retorna um valor do tipo contido na lista
lista.append(50)
lista.append(60)
lista.append(70)
print(lista)

# Removendo o ultimo elemento da lista 
ultimo_valor = lista.pop()
print(lista, '\nRemovido foi:', ultimo_valor)

# Quando a lista for cura, também podemos remover os indices do meio com o pop

ultimo_valor = lista.pop(3)
print(lista, '\nRemovido foi:', ultimo_valor)




