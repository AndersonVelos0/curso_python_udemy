'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''

ganhos_por_hora = float(input('Digite quanto é o valor da sua hora: '))
horas_trabalhadas = float(input('Digite o numero de horas em que você trabalha no mês: '))

salario_bruto = ganhos_por_hora * horas_trabalhadas

desconto_imposto = 0.11 * salario_bruto 
desconto_inss = 0.08 * salario_bruto  
desconto_sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - desconto_imposto - desconto_inss - desconto_sindicato


print(f'+ Salário Bruto: R${salario_bruto: .2f}')
print(f'- IR (11%): R${desconto_imposto: .2f}')
print(f'- INSS (8%): R${desconto_inss: .2f}')
print(f'- Sindicato (5%): R${desconto_sindicato: .2f}')
print(f'= Salario Liquido: R${salario_liquido: .2f}')

