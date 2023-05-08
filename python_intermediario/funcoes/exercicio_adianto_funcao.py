# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y

# Na função abaixo, foi criada uma outra função interna, onde recebe o y(parametro faltante)
# e utiliza o closure para guardar os parametros da primeira, onde, quando chamada executará tudo
# portanto, quando a criar_funcao é chamada
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

# Aqui os primeiros parametros são passados e guardados em criar_funcao
soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

# Utilizando o closure, passamos o parametro faltante e a função será executada
print(soma_com_cinco(10))
print(multiplica_por_dez(10))