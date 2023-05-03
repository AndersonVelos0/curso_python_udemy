# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(d):
    if d == 0:
        # Raise cria uma exceção e levanta uma mensagem que você mesmo lançou
        # É chamado de relançar uma exceção
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    # Se n não tiver instanciado nem em float, nem em int, a exceção será levantada
    if not isinstance(n,(float,int)):
        raise TypeError(
            f'"{n}" deve ser int ou float'
            f'"{tipo_n.__name__}" enviado!'   
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

# Levantará a exceção 
print(divide(8, '0'))