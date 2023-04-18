"""
For + Range
range -> range(start, stop, step)
"""

# passa o start, o stop e o step
# pode ser negativo e positivo, mas tem que inverter
numeros = range(0,21,2)

# For não está pegando o indice e sim, o valor
# Para cada iteração em numeros, ele lançará um numero para {numero}
for numero in numeros:
    print(numero)