# reduce - faz a redução de um iterável em um valor
# Reduz valores em um unico valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]




# Imagine que eu queira o valor total dos produtos acima 

# Simples 

# total = 0 
# for p in produtos:
#     total += p ['preco']
    
# print(total)

# Pegando total com o reduce

def funcao_do_reduce(acumulador, produto):
    print('Acumulador', acumulador)
    print('Produto', produto)
    print()
    return acumulador + produto['preco']

# Criando a função de cima com lambda
# Passa uma função, iteravel e o inicial
total = reduce(lambda ac, p: ac + p['preco'], produtos, 0)
print(total)