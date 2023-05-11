# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Quando tiver problemas que gerem loops, for, while, geralmente
# podem ser convertidos em funções recursivas
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm


# Criando uma função recursiva simples 
# # Contando de um numero até outro numero
# def recursiva(inicio = 0, fim = 10):
#     # Caso recursivo
#     # contar até chegar o final
#     inicio += 1
#     return recursiva(inicio, fim)

# recursiva()

# Nesse caso, ocorre o stack overflow, onde a recursão está retornando uma 
# nova função a cada ciclo, onde carrega muita coisa na memória


# Corrigindo o erro acima, precisamos de um caso base


def recursiva(inicio = 0, fim = 10):
    # Caso base
    if inicio >= fim:
        return fim 
    print(inicio, fim)
    # Caso recursivo
    # contar até chegar o final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())