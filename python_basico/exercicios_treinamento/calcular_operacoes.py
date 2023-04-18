'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

inteiro1 = int(input('Digite um numero inteiro: '))
inteiro2 = int(input('Digite outro numero inteiro: '))
real1 = float(input('Digite um numero real: '))

produto_do_dobro = (inteiro1 * 2) * (inteiro2 / 2)
soma_do_triplo = (inteiro1 * 3) + real1

print(f'O produto do dobro do primeiro com metade do segundo é: {produto_do_dobro: .2f}')
print(f'A soma do triplo do primeiro com o terceiro é: {soma_do_triplo: .2f}')