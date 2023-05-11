# filter é um filtro funcional


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


def filtrar_preco (produto):
    return produto['preco'] > 100

# Aqui estou pedindo todos os produtos maiores que 10
novos_produtos = [
    p for p in produtos
    if p['preco'] > 100 
]
print_iter(produtos)
print_iter(novos_produtos)

# Utilizando filter onde vai retornar todos os produtos maiores que 10
novo_produto = filter(
    # lambda p: p['preco'] >= 10, produtos
    # Não é necessário executar a função, o python já faz isso 
    filtrar_preco, produtos
    )

print_iter(novo_produto)