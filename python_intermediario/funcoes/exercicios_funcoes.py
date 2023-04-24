# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 2


# Criando o exemplo de forma mais dinamica e complexa
# A função abaixo passa como parametro um multiplicador, que cria a função multiplicar
# para que o numero seja multiplicado utilizando a logica do closure 
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

# Para ativarmos e executarmos a função multiplicar, devemos fechar os parenteses e passar o argumento
print(duplicar(2))
print(triplicar(3))
print(quadruplicar(4))