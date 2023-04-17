"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
# método para adicionar caracteres a esquerda da variavel
print(f'{variavel: >10}')
# método para adicionar caracteres a direita da variavel
print(f'{variavel: <10}.')
# método para adicionar caracteres a direita da variavel
print(f'{variavel: ^10}.')
# método para adicionar zeros antes do numero e filtrar com apenas 1 casa decimal
print(f'{1000.4873648123746:0=+10,.1f}')
# método para adicionar caracteres ao numero hexadecimal
print(f'O hexadecimal de 1500 é {1500:08X}')
# método está se referindo ao método rapper
print(f'{variavel!r}')