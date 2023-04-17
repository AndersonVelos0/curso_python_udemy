"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = input('Digite seu nome:')

# Como fiz
contador = 0
while contador <= len(nome):
    print(f'*{nome [contador]}*')
    contador += 1

print('Acabou!')

# Modelo do professor

nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)