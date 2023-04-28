# dir, hasattr e getattr em Python

# Utilizando o debuger console e digitando dir(variavel) ele abre todas as opções disponiveis para aquele tipo 

string = 'Luiz'
metodo = 'casefold'

# Hasattr checa se existe um método dentro do objeto 
if hasattr(string, metodo):
    print('Existe upper')
    # O getattr irá checar se existe o método proposto e irá chamá-lo mediante o nome na variavel
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
