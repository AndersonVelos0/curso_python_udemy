"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    numero = input('Digite um numero: ')
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O numero é par')
    else: 
        print('O numero é impar')


except:
    print('Isso não é um numero inteiro')        

