"""
enumerate - enumera iteráveis (índices)

"""
# 
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# Utilizando o método enumerate para numerar os valores da tupla
# Caso você queira mostrar os valores dos indices, pode converter para uma lista ou para uma tupla
# lista_enumerada = list(enumerate(lista, start=20))
# print(lista_enumerada)
# Consumindo os valores da lista no for 
# for item in lista_enumerada:
#     print(item)
# # Apenas restará o iterator, pois os valores ja foram consumidos
# print('O que tem na minha lista enumerada:', lista_enumerada)

# Podemos contornar esse problema utilizando o enumerate diretamente sem jogar em nenhuma variavel
for item in enumerate(lista):
    print(item)



# Ele criará um for dentro de outro separando pelo indice e pelo nome
for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')