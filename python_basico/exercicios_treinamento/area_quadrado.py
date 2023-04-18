'''

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

'''

base = float(input('Digite o valor do raio: ')) 
altura = float(input('Digite o valor da altura: ')) 

area_quadrado = base * altura


print(f'A area do quadrado é:{area_quadrado:.2f} e o dobro da área é: {area_quadrado * 2}')