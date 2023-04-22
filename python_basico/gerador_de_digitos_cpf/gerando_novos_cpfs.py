
# importando o módulo para coisas aleatorias
import random

# utilizando o random int, onde você passa os parametros da contagem inicial até a final

for _ in range(100):
    nove_digitos = ''

    # Criando um for para 9 digitos com 9 iterações
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    contador_regresso_1 = 10
    resultado_1 = 0
    # Para cada digito em nove digitos
    for digito_1 in nove_digitos:
        resultado_1 += int(digito_1) * contador_regresso_1
        contador_regresso_1 -= 1


    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    # print(digito_1)




    # Calculando o segundo digito do CPF

    # Adicionando o digito 1 na string tornando-a com 11 indices
    dez_digitos = nove_digitos[:9] + str(digito_1)

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
    print(cpf_gerado_pelo_calculo)
