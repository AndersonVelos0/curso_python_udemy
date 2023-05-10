# count é um iterador sem fim (itertools)

# Contador infinito, ele é um interador
# Diferente do range que tem fim e não é um interador

# Você informa ao count quando ele começa, pode passar os passos, etc


# Importando o método intertools

from itertools import count 

c1 = count(start= 8, step=8)
r1 = range(10,100, 8)

# Verificando se é um itator e um iteravel
print(c1, hasattr(c1, '__iter__'))
print(c1, hasattr(c1, '__nex__'))
print(r1, hasattr(c1, '__iter__'))
print(r1, hasattr(c1, '__nex__'))


# Temos que limitar o count

print('Count')
for i in c1:
    if i > 100:
        break
    print(i)

# Fazendo a mesma coisa com o range

print('Range')
for i in r1:
    if i > 100:
        break
    print(i)
