# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

# Convertendo os tipos str em int
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

# Também poderia ter sido feita a conversão na propria linha do input
# Contudo, iria apresentar uma quebra nas boas praticas
# numero_1 = int (input('Digite um número: '))
# numero_2 = int (input('Digite outro número: '))

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')