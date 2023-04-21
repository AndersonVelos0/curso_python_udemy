"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Olha só que, coisa interessante'
# utilizando um método dentro da string
# lista_palavras = frase.split()
# Separando pela virgula da frase
lista_frases_original = frase.split()

lista_frases = []
for i, frase in enumerate(lista_frases_original):
    # Tirando os espaços do começo e do fim da string
    lista_frases.append(lista_frases_original[i].strip())
    # também tem r strip que corta os espaços da direita e l strip que corta os da esquerda

# Printa a nova lista sem que você altere a lista original
print(lista_frases)

# Unindo as frases utilizando JOIN e passando o divisor
frases_unidar = ': '.join(lista_frases)
print(frases_unidar)