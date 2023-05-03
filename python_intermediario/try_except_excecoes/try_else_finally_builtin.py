# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO')
    8/0

# Capturando o erro com o as e uma variavel
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
# Pode chamar após o try 
else:
    print('Não deu erro')

# Pode chamar após o try
finally:
    print('FECHAR ARQUIVO')