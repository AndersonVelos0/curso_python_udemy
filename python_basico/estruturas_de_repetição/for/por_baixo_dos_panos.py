"""
Iterável -> str, range, etc (__iter__) (é um objeto, com método iter)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Anderson'  # iterável, é um elemento que sabe entregar um elemento por vez na string

# iteratador = iter(texto)  # iterator

# while True:
#     try:
            # função next entrega o proximo valor da string, dentro do iteravel
#         letra = next(iteratador)
#         print(letra)
#     except StopIteration:
#         break

# Quando chamamos o for, ele irá verificar quem é o texto e aplicar o método iter no texto e solicita o objeto iterador
# em seguida dentro do for, ele irá solicitar o método next
for letra in texto:
    print(letra)
