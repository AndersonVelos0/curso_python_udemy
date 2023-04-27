# Mapeamento de dados em list comprehension 

"""
Mapeamento em listas significa que você terá a primeira lista criada, 
com um tamanho estabelecido, uma nova lista criada terá o mesmo tamanho da lista anterior
os valores podem ser mudados, contudo, os indices serão mapeados, você está pegando os dados iteraveis
da primeira lista e mapeando com a segunda, devem ter o mesmo tamanho
"""


lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(list(range(10)))
# print(lista)



# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# Mapeando em uma nova lista para mapeamento
# Temos um novo dicionario para alteração de preço
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    # o if a esquerda do for é utilizado para mapeamento
    # caso o produto seja maior que 20, ele vai aplicar a variação, caso não, retorna o dicionario
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')
