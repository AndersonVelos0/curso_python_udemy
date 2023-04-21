"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Anderson', 'Bia', 1, True, 1.2]

# Referenciando um mesmo valor na memória e não copiando-os
# Mesmo não alterando nada na lista B, o valor inserido na A aparece, pois estão sendo referenciados no mesmo espaço de memória
# lista_a[0] = 'Beatrice'
# lista_b = lista_a
# print(lista_b)

# Quando é um valor IMUTAVEL eu copio com sinal de igual
# Quando é um valor MUTAVEL eu estou apontando para o mesmo valor na memoria

lista_a = ['Anderson', 'Bia', 1, True, 1.2]
# Copiando os dados da lista A com método copy
lista_b = lista_a.copy()
# Verificando que a lista agora esta copiada e não referenciada no mesmo espaço
lista_a [0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
