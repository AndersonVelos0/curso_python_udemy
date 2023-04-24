"""
Higher Order Functions
Funções de primeira classe
"""

# As funções FIRST CLASS functions em python podem ser tratadas como qualquer tipo de dados
# Já as higher ordes functions recebem outras funções como parametro

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

# A função executa irá executar a função saudacao e o resto está passando parametros desconhecidos no final, caso queira adicionar
def executa(funcao, *args):
    # Há o desempacotamento abaixo
    return funcao(*args)

# É possivel passar uma função como parametro de outra funçao
print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)


# Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

# Higher Order Functions - Funções que podem receber e/ou retornar outras funções

# First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

# Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

# Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.