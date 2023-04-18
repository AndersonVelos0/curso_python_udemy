# For é mais utilizado para repetições previstas
# While não se tem numeros de repetições previstos

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')



# Iterando sobre a string
# A variavel letra é criada por você, algo como um for each
# iteravel entrega um valor por vez
# o for solicita o iterador (letra)
# para cada letra em texto(iteravel), faça:

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

   
print(novo_texto + '*')