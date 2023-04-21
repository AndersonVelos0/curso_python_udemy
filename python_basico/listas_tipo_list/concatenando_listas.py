"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista_a = [1,2,3,4,5]
lista_b = [6,7,8,9]
# Lista C é a uniao da lista a com a lista b
lista_c = lista_a + lista_b
# Lista a chama o método extend
lista_a.extend(lista_b)
print(lista_a)
# Na forma acima ele está efetuando a ação diretamente na lista a
# Devido a isto, não podemos atribuir a nenhuma outra variavel