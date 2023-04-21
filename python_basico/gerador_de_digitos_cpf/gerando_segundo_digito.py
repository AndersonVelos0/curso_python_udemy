"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""
# Importando regular expression
import re
# Importando o sys 
import sys

cpf_usuario = input('Digite o seu cpf: ')\
            # .replace('.', '')\
            # .replace(' ', '')\
            # .replace('-', '')  
# Utilizando regular expression para substituir
# primeiro é passado o r de expressão regular 
    # tudo que não for um numero substitua por, significado da expressão abaixo
Cpf_formatado = re.sub(r'[^0-9]', '', cpf_usuario )
# Verificando se há digitos iguais
entrada_e_sequencial = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)

# Caso entre nessa lógica, o código irá parar
if entrada_e_sequencial:
    print('Você enviou dados sequenciais!')
    sys.exit()


nove_digitos = cpf_usuario[:9]

contador_regresso_1 = 10
resultado_1 = 0
# Para cada digito em nove digitos
for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * contador_regresso_1
    contador_regresso_1 -= 1


digito_1 = (resultado_1 *10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
# print(digito_1)



# Calculando o segundo digito do CPF
 
# Adicionando o digito 1 na string tornando-a com 11 indices
dez_digitos = cpf_usuario[:9] + str(digito_1)

contador_regresso_2 = 11
resultado_2 = 0

for digito_2 in dez_digitos:
    resultado_2 += int(digito_2) * contador_regresso_2
    contador_regresso_2 -= 1

# print(resultado_2)

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
# print(digito_2)

# Gerando o novo cpf 

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
# print(cpf_gerado_pelo_calculo)

if cpf_usuario == cpf_gerado_pelo_calculo:
    print('CPF enviado pelo usuário é válido!')
else:
    print('O CPF enviado não é valido!')
