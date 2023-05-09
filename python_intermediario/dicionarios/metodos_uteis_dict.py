# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
pessoa = {
    'nome':'Anderson',
    'sobrenome': 'Miranda',
    # 'idade': 900,
}
# Função len que chama o método dunder len __len__
print(len(pessoa))
print(pessoa['nome'])

# Função para retornar as chaves do dict 
# Você pode retornar no tipo que preferri
print(pessoa.keys())
print(list(pessoa.keys()))

#Retornando os valores
print(list(pessoa.values()))

# Retornando as chaves e o valor 
print(list(pessoa.items()))

# Caso uma chave não exista e você queira definir um valor padrão para defini-la, utilizamos setdefault 
pessoa.setdefault('idade', 20)
print(pessoa['idade'])

# Esse for do enumerate faz a mesma coisa que a função items
for chave, valor in pessoa.items():
    print(chave, valor)