# groupby - agrupando valores (itertools)
# Os dados precisam estar ordenados para utilizar o groupby 

from itertools import groupby


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


# Criando uma função que retorna o dicionario pela nota
def ordena (aluno):
    return aluno['nota']

# Utilizando lambda como key para ordenar pela nota
alunos_agrupados = sorted(alunos, key= ordena)
grupos = groupby(alunos_agrupados, key= ordena)

# Consumindo a copia rasa da lista
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

# grupos = groupby(alunos)

# # O groupby retorna uma tupla, chave e valor, segue exemplo

# # Ele agrupará todos os 'a' em um só 
# alunos = ['a','a','a','a', 'b', 'c']
# grupos = groupby(sorted(alunos))

# # Ele retorna um iterator, portanto, faremos um for para consumir
# # Ele retornará o chave e valor
# for chave, grupo in grupos:
#     print(chave)
#     # Mostrando a chave e os valores
#     print(list(grupo))


