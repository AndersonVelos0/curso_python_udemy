'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

'''

celsius = float(input('Digite a temperatura em graus celsius: '))
CONSTANTE = 1.8

fahrenheit = float((celsius * CONSTANTE) + 32)

print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}')