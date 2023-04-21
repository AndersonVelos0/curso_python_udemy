"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1


# Utilizando o tipo da lista é List (uma lista de coisas, uma matriz)

# uma das formas de usar
lista = list()
#         0,   1,       2,              3,   4
lista = [123, True, 'Anderson Veloso', 1.5, []]
print(lista, type(lista))
lista [-3] = 'Andersin'
# Checando os tipos especificos dos indices 
print(lista[2].upper(), type(lista[2]))

