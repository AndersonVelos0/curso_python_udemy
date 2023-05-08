# Variavel Livres + NonLocal


# A função fora comporta uma variavel a que é livre, ja a função dentro retorna a, mas não pode alterá-lo
def fora(x):
    # A variavel a é uma variavel livre
    a = x
    
    def dentro():
        # a função locals retorna as variaveis locais dentro do escopo
        # print(locals())
        return a 
    return dentro

# testando as funções  
dentro1 = fora(10)
dentro2 = fora(20)

# Retorna os valores passados como parametro na função fora e executa eles pelo closure
# print(dentro1())
# print(dentro2())


# Criando uma função onde é possível alterar o valor da variavel com o método nonLocal

def concatenar(string_inicial):
    valor_final = string_inicial
    
    def interna(valor_a_concatenar):
        # utilizando o nonlocal para permitir a modificação
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
# # Abaixo dará erro, devido a necessitar de um argumento obrigatório
# final = c()
# print(final)
        