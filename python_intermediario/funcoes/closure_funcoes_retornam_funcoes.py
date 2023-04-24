"""
Closure e funções que retornam outras funções
"""



def criar_saudacao(saudacao):
    # Nome será um parametro dinamico para adicionar só na chamada da função
    def saudar(nome):
        return f' {saudacao}, {nome}!'
    return saudar

# Ao retirarmos os parenteses de saudar, o python apenas salva os valores passados nos argumentos, mas não executa a função
# a função passa pelo closure e somente é executada quando fechamos os parenteses no print das linhas 18,19
# o escopo de saudar fica salvo em call stack e quando a função for executada ele puxará os valores armazenados na memoria

# Caso você não queira ficar repetindo essas expressões, pode-se utilizar o CLOSER
falar_bom_dia = criar_saudacao('Bom dia') 
falar_boa_noite = criar_saudacao('Boa noite') 


for nome in ['Anderson', 'Beatriz', 'Gabriella']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

