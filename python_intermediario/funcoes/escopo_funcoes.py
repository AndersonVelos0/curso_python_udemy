"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos. 
A palavra global faz uma variavel do escopo externo ser a mesma do 
escopo interno
"""

# Quando x é criado aqui o escopo é do módulo e dentro da função, é o escopo local
x = 1

# Criando uma função para passar uma variavel dentro do escopo dela
def escopo():
    global x
    # X só existe dentro da função, a menos que seja criado fora dela
    # x = 1 
    def outra_funcao():
        # essa variavel declarada não poderá ser vista pela função escopo, nem pelo escopo do módulo
        # pois ela só existe dentro desta função
        y = 2
        print(x, y)
    outra_funcao()    
    print(x)

escopo()


# O passo a passo de cima será, ele irá executar a função escopo, em seguida irá 
# rodar a outra_funcao, ler o código, em seguida irá executá-la e finaliza com a função escopo
# Os escopos das funções tem suas variaveis guardadas dentro do escopo local
# Algo se assemelha a uma boneca russa, com cada camada fechada
# Do escopo interno, podemos acessar o escopo externo