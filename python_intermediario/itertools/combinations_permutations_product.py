# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos


# Importando o módulo itertools com o combination 
from itertools import combinations, permutations, product

# Criando uma função para replicar isso outras vezes

def print_iter(iterator):
    print(*list (iterator), sep = '\n')

pessoas = [
    'Joao', 'Ana', 'Beatriz', 'Anderson',
]

camisetas = [
    ['Preta', 'Branca'],
    ['p', 'm', 'g'], 
    ['Masculino', 'Feminino'], 
    ['Poliester', 'Algodao']
]

# Escolhendo apenas duas combinações na lista
# Passando a combinação de grupos de dois itens da lista
# Ele retornará um iterator, no qual a gente pode consumir com uma lista
# print_iter(combinations(pessoas, 2))
# print()

# Permutations agora, para verificar todas as combinações possiveis
# print_iter(permutations(pessoas , 2))

# Utilizando o produto, a lista cresce exponencialmente e combina tudo 
print_iter(product(*camisetas))
