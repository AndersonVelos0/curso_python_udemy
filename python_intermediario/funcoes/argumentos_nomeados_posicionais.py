"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# Criando a função com parametros
def soma(a,b,c):
    print(f'{a=} {b=} {c=}', '|', 'a + b +  = ', a + b + c)

# Chamando a função passando os argumentos não nomeados  (POSICIONAIS) 
soma (10,20,2)
# Chamando a função passando argumentos nomeados
soma (b=10, a = 90, c=10)

# Todas as vezes que você chama um argumento nomeado, os proximos devem ser nomeados
soma(1,b=2, c=3)
