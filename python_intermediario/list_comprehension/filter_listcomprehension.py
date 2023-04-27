import pprint

# Função para organizar o print bonito
def p(v):
    pprint.pprint(v, sort_dicts= False, width= 40)


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
# print(*novos_produtos, sep='\n')
# p(novos_produtos)


# Filtrando uma lista com list comprehension
# Filtro é após o for, diferente de map, e não possui else
# O for abaixo irá incluir o numero se a condição for true, e não inclui se for false
# lista = [n for n in range(10) if n < 5]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    # o if a esquerda do for é utilizado para mapeamento
    # caso o produto seja maior que 20, ele vai aplicar a variação, caso não, retorna o dicionario
    if produto['preco'] > 20 else {**produto}
    for produto in produtos if produto['preco'] >= 20 and produto ['preco'] * 1.05 > 10 
]


p(novos_produtos)


# RESUMO 

# Mapeamento é quando você pode pegar um dado, transformando-o em uma nova lista DE MESMO TAMANHO
# Filtro quer dizer que você pode incluir ou não aquele elemento mapeado na sua nova lista e as duas coisas podem ser unidas



