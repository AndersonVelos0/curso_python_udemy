a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
# Função format serve para formatar uma string introduzindo variaveis dentro das chaves
formato = string.format(
    # abaixo temos um parametro nomeado, onde se refere ao nome da variavel
    nome1=a, nome2=b, nome3=c
)

print(formato)