'''

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.

'''

ganhos_por_hora = float(input('Digite quanto é o valor da sua hora: '))
horas_trabalhadas = float(input('Digite o numero de horas em que você trabalha no mês: '))

salario_total = ganhos_por_hora * horas_trabalhadas

print(f'O seu salario mensal é: R${salario_total:.2f}')