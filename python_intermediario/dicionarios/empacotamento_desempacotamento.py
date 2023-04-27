# Empacotamento e desempacotamento de dicionários
# Desempacotando o valor de a e o de b nas variaveis a e b 
a, b = 1, 2
a, b = b, a
print(a, b)


# Tentando desempacotar dicionarios 

pessoa = {
    'nome': 'Anderson', 
    'sobrenome': 'Veloso',
}
# # Retorna as chaves, somente
# a, b = pessoa
# print(a,b)
# # Passando o values para retornar os valores dentro das chaves
# a, b = pessoa.values()
# print(a,b)
# # items também pode ser utilizado para retornar uma tupla com nome e sobrenome, chave e valor
# a, b = pessoa.items()
# print(a,b)

# # Também é possível desempacotar internamente os dicionarios
# (a1,a2), (b1,b2) = pessoa.items()
# print(a1,a2)
# print(b1,b2)

# # Isso é semelhante ao for 
# for chave, valor in pessoa.items():
#     print(chave, valor)




# UTILIZANDO ARGS E KWARGS 
# args (já foi visto na seção)
# kwargs = Keyword arguments (argumentos nomeados)

# Como posso unir os dois dicionarios abaixo?
pessoa = {
    'nome': 'Anderson', 
    'sobrenome': 'Veloso',
}

dados_pessoas = {
    'idade': 16,
    'altura': 1.77,
}

# Criando um terceiro dicionario para extrair os valores dos dicionarios acima
# Utilizando a função kwargs para empacotar dois dicionarios com **
pessoa_completa = {**pessoa, **dados_pessoas}
print(pessoa_completa)

# kwargs vão se referir aos argumentos nomeados

# Criando uma função para representar o uso dos kwargs junto com args

def argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)
    
    # Criando um for para vermos as chaves e valores
    for chave, valor in kwargs.items():
        print(chave, valor)

# Os argumentos não nomeados ficam isolados dos nomeados
# argumentos_nomeados(1,2,3, nome = 'Anderson', idade = 16, altura = 1.77)
# Desempacotando uma chamada de função passando os kwargs
argumentos_nomeados(**pessoa_completa)
