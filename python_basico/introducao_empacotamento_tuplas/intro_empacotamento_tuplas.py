"""
Introdução ao empacotamento e desempacotamento
"""

# Temos uma "Sacola de nomes abaixo"
# Vamos desempacotar
nomes = ['Maria', 'Helena', 'Luiz']
# Desempacotando os valores atribuindo a variaveis, porem um erro será gerado
# Pois não temos variaveis suficientes para atribuir os valores da lista
# ValueError: too many values to unpack (expected 2)
# ValueError: not enough values to unpack (expected 4, got 3)
# nome1, nome2, nome3, nome4 = nomes
# nome1, nome2, nome3 = nomes

# Para desempacotar fazemos da seguinte forma:

nome1, nome2, nome3 = nomes
print(nome1)

# Desempacotando apenas um valor e empacotando o restante
_, nome2, *_ = nomes
print(nome2)