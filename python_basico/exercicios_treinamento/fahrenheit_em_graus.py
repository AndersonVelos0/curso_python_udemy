'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''

farenheit = float(input('Digite a temperatura em farenheit: '))

celsius = 5 * ((farenheit-32) / 9)

print(f'A temperatura em graus celsius é: {celsius:.2f}')