# Problema dos parâmetros mutáveis em funções Python
# Não se deve começar uma lista com parametro mutavel lista = [] pois o python utiliza a mesma lista
# Não se deve utilizar argumentos mutaveis, se for mutavel, utilize um none, podendo checar e criar uma nova lista quando uma não for passada
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

# formas de não utilizar a mesma lista

lista1 = []
cliente1 = adiciona_clientes('Jorge', lista1)
adiciona_clientes('Pedro', lista1)
print(cliente1)

# Forma que utiliza a mesma lista do parametro da func 
cliente2 = adiciona_clientes('Maria')
adiciona_clientes('Elizangela', cliente2)
print(cliente2)