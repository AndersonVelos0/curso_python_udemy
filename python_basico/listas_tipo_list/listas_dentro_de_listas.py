"""
Lista de listas e seus índices
"""

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda'],  # 2
]
# (0,10,20,30,40)
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

# para cada sala na lista salas, me retorne a sala
for sala in salas:
    print('A sala é: ', sala)
    # para cada aluno na sala, me retorna o aluno
    for aluno in sala:
        print('Os alunos da sala são: ', aluno)

