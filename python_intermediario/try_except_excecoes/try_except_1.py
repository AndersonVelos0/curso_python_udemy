# (Parte1) try e except para tratar exceções


# Se tentarmos dividir por zero, não será possivel 
# levantará uma exceção

# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
    
# Criando as exceções com os erros levantados e tratados
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except NameError:
    print('Nome b não está definido')

# Podemos tratar dois erros em uma linha só passando uma tupla
# Abaixo cria uma varaivel para receber a instancia do alias(criar uma variavel)"as"
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    # abaixo nós colocamos o erro em mensagem para saber qual ocorreu
    print('MSG:', error)
    # colocando a classe do erro e retornando o nome do erro
    print('Nome:', error.__class__.__name__)
    
# Classe superior de erro no python, irá tratar qualquer outro erro
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
