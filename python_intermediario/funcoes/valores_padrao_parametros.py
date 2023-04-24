"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(x+y)
    

soma(1,2)
soma(800,300)
soma(800,1000)


# Caso você queira declarar mais outro valor, contudo, ele não aparecerá por ser falsy 


def teste_soma(x, y, z=0):
# O if não irá aparecer, pois ele é um valor falsy e a condicional já o ignora automaticamente
# Caso queiramos contornar, podemos atribuir um valor None a Z e perguntar ao if se ele é none ou nao
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=} ', x + y)
        
# Ainda que o parametro tenha sido definido na função, ele se torna um não valor 
teste_soma(800,300, 0)
soma(800,1000)
teste_soma(x = 15, z=0, y=10)
teste_soma(x = 15, z=10, y=10)
