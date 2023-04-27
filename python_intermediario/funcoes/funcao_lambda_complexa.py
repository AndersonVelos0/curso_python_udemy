
# Tudo que você usa nas funções normais podem ser utilizadas nas funções lambdas
# Pela pep-8 fala para criar uma função para executar o lambda 


# Recebe qualquer argumento não nomeado e retorna a função executada
def executa(funcao, *args):
    return funcao(*args)

# Soma dois parametros passados
# def soma(x, y):
#     return x + y

# # Multiplica um numero pelo seu multiplicador 
# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica

# Criando uma função lambda para somar dois numeros

# lambda não tem nome, não tem parenteses e só os argumentos, não necessita de return, ela já retornará

print(
    
    executa(
        # qualquer função que tiver dois parametros será igual a essa função lambda
        lambda x,y: x + y, 
        # Passando os parametros
        2,3
    ), 
    # executa(soma,2,3), 
    # soma(2,3)
    #as linhas acima são a mesma coisa
)

# Criando uma função que retorna outra função e criando um multiplicador
duplica = executa(
        lambda m: lambda n: n * m,
        2
)
print(duplica(2))

# Função para somar todos os argumentos com lambda que também aceita *args

print(executa(lambda *args: sum(args), 1,2,3,4,5,6,7))


# Lembrando que, lambda é utilizado para coisas simples