"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
# importando a biblioteca decimal
import decimal

# Só utilize decimal para precisões muito detalhadas
numero1 = decimal.Decimal('0.1')
numero2 = decimal.Decimal('0.7')
numero_3 = numero1 + numero2
# O valor nao será representado precisamente no exemplo abaixo
print(numero_3, type(numero_3))
# Como contornar com a função round passando a variavel e o numero de casas
print(round(numero_3, 1))
print(f'{numero_3:.1f}')