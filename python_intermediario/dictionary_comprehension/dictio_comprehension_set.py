# Dictionary Comprehension e Set comprehension 
# Tudo em list comprehen


# Criando um dicionario
produto = {
    'nome': 'Caneta Azul', 
    'preco': 2.5,
    'categoria': 'Escritório',
}

# mostrando chave e valor com for 
for chave, valor in produto.items():
    print(chave,valor)
    
    
# utilizando dictionary comprehension
dicionario = {
    # na dict comprehension abaixo estamos fazendo as validações com if
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave,valor in produto.items()
}

# Caso eu queira gerar um dicionario a partir de uma lista com chave e valor
lista = [
    ('a', 'valor a '),
    ('b', 'valor b '),
    ('c', 'valor c ')
]

# dicionario = {
#     chave: valor for chave,valor in lista
# }

# Também podemos converter usando o dict
print(dict(lista))
print(dicionario)


# Set comprehension 
s1 = {i * 2 for i in range(10)}
# também é possivel FAZER desta forma
# print(set(range(10)))

print(s1)