
# Manipulando as chaves do dicionario

pessoa = {
    # devemos indicar os indices e os dois pontos valem como um igual = 
    'nome': 'Anderson Veloso',
    'sobrenome': 'Luna',
    'idade': 18,
    'altura': 1.8,
    # Dentro do dicionario de endereços, tem uma lista de endereços
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
    
}

# Criando um dicionario e adicionando uma chave e um valor a ela 
# O mesmo é utilizado para alterar o valor da chave
pessoa ['casa'] = 'Casa 1'
print(pessoa['casa'])

# apagando um valor de uma chave 
del pessoa['casa']
# print(pessoa['casa'])
# KeyError: 'casa' 

# Não queremos que o erro seja gerado, então utilizamos o método get do dicionario para verificar se a chave existe ou não
# sem que o programa quebre

if pessoa.get('casa') is None:
    print('A chave não existe')
else:
    print('A chave existe')