"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

# Isso é feito para uma quantidade inimaginavel de parametros passados pelo usuario
# Args empacota o que for enviado para função dentro de uma tupla
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)


# a variavel numeros é uma tupla empacotada
numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
# A variavel numero é desempacotada em uma tupla dentro da função soma
outra_soma = soma(*numeros)
print(outra_soma)

# Função sum faz o papel do iteravel e soma os numeros dentro da tupla
print(sum(numeros))
# print(*numeros)