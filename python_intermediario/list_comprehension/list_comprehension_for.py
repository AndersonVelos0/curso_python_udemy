# List comprehension com mais de um for dentro 

lista = []
for x in range(3):
    for y in range(3):
        # adicionando uma tupla na lista
        lista.append((x,y))
#print(lista)

# Em list comprehension agora
# o lado esquerdo do for sempre será utilizado para mapeamento
lista = [
    (x,y) for x in range(3)
    for y in range(3)
]

# Outra forma que também pode ser criada é uma list comprehension dentro de um valor da list comprehension
lista = [
    [(x,letra) for letra in 'ola']
    for x in range(3)
]

print(lista)
        