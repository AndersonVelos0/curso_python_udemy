"""
Tipo tupla - Uma lista imutável
É um pouco mais eficiente que a lista
"""

# Criando um tipo de dados tuple, sem colchetes
nomes = ['Maria', 'Helena', 'Luiz']
# convertendo uma lista para tupla
nomes = tuple(nomes)
print(nomes)
# convertendo uma tupla em lista
nomes = list(nomes)
print(nomes[0])
print(nomes)


# O erro seguinte será gerado caso tentemos alterar algum valor da tupla:
# TypeError: 'tuple' object does not support item assignment
# nomes[1] = 'Outro'

