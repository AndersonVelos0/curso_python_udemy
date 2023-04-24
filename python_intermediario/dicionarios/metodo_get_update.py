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
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# Para obter a chave com get podemos fazer o seguinte
print(p1.get('nome'))

# Pop apaga um item com uma chave identificada
# nome = p1.pop('nome')
# print(nome)
# print(p1)

# PopItem elimina a ultima chave do dicionario
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

# Atualizando o dicionario com update, você pode criar, atualizar 
# Temos 3 formas

p1.update({
    
        'nome': 'Dersinho', 
        'sobrenome': 'Veloso', 
        'idade': 35, 
        
})
print(p1)

# Outra forma
p1.update(nome= 'Outro nome', sobrenome = 'Luna', idade = 23)
print(p1)

# outra forma passando uma tupla e uma lista
tupla = (('nome','novo valor'), ('idade', 25))
tupla = [['nome','novo valor'], ['idade', 22]]
p1.update(tupla) # // LISTA TAMBEM FUNCIONA
print(p1)