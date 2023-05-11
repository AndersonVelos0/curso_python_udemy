# map, partial, GeneratorType e esgotamento de Iterators


# Importando os módulos 
# São ferramentas para as funções
# Partial é uma função que vai receber uma função 
from functools import partial
# GENERATORTYPE checa se é uma instancia de generatortype
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Função pra calcular o preço e aumentar de acordo com a porcentagem passada
def aumentar_porcentagem(valor,porcentagem):
    return round(valor * porcentagem)

# Utilizando o parcial, cria uma função que recebe outra função
aumenta_dez_porcento = partial(aumentar_porcentagem, porcentagem = 1.1)

# # Utilizando list comprehension 
# novos_produtos = [
#     {**p, 'preco': aumenta_dez_porcento(p['preco'])} for p in produtos
# ]


# Função para mudar o preco dos produtos
def muda_preco_produto (produto):
   return {**produto, 'preco': aumenta_dez_porcento(produto['preco'])}

# Utilizando a função map para mapear os dados
# o map precisa de uma função que faz algo 
# Map recebe uma função no primeiro parametro e um iteravel no segundo
novos_produtos = map(muda_preco_produto, produtos)

print_iter(produtos)
print_iter(novos_produtos)
print(isinstance(novos_produtos, GeneratorType))


print(list(map(lambda x: x *3, [1,2,3,4,5])))