# List comprehension 

# List comprehension é uma forma rápida de criar listas 
# a partir de iteraveis

# criando uma lista com range
print(list(range(10)))

lista = []
# Criando uma lista com um for
for numero in range(10):
    lista.append(numero)
print(lista)

# Fazendo as mesmas linhas de código acima utilizando list comprehension
# Você pode fazer lógicas dentro da list comprehension
lista = [numero * 2 for numero in range(10)]
print(lista)
