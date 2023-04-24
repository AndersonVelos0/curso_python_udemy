# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
    

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total



print(multiplica(1,2,3))


def par_ou_impar(a):
    if a % 2 == 0:
        print(f'O numero {a} é par')
    else:
        print(f'O numero {a} é ímpar') 
        
    return a   

par_ou_impar(11)