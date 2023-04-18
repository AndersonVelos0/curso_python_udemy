'''

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

'''


raio = float(input('Digite o valor do raio: '))
PI = 3.14 

area_circunferencia = PI * (raio ** 2)

print(f'A area da circunferencia é:{area_circunferencia:.2f}')