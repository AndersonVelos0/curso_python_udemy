# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# Iterando sobre os dados da lista pegando o primeiro e ultimo dado
# Desempacotando em chamada de funções
p,b,*_, u = lista
print(p,u )

# Iterando sobre os itens da lista 
for nome in lista:
    print(nome, end = ' ')

# Iterando sobre cada um dos itens utilizando só a função print 
print(*string)
print(*lista)

print(*salas, sep ='\n')