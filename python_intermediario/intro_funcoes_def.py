# Introdução as funções em Python 

"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# definindo uma função

def Print():
    print('Ola mundo!')
    print('Ola mundo!')
    print('Ola mundo!')
    print('Ola mundo!')

string = Print()


# Passando valores de parametros
def Print2(a,b,c):
    print('Passei os parametros da função Print2!')

Print2(1,2,3)

# Utilizando os parametros dentro da função 
def Print3(a,b,c):
    print(f'Os argumentos passados foram: {a},{b},{c}')

Print3(15,40,20)
