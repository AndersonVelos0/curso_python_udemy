"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        # Se x for
        return 10, 20
    # Return diz, para tudo que voce ta fazendo e retorna o que eu to mandando
    return x + y
# Quando não colocamos o return, a função tem por padrão um valor None, o mesmo vale para o print
# Que foi criado apenas para exibir algo na tela

# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))