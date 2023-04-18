'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas
'''

REGULAMENTO = 50
MULTA = 4

peso_do_peixe = float(input('Digite o peso do peixe: '))

if peso_do_peixe > REGULAMENTO:
    excesso = peso_do_peixe - REGULAMENTO
    pagamento = excesso * MULTA
    print(f'O peso do peixe foi: {peso_do_peixe}')
    print(f'O excesso de kilos foi: {excesso}')
    print(f'O valor da multa foi: {pagamento}')
    
else:
    print('O peixe está dentro dos conformes')

