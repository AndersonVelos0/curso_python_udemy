'''
### Exercício 2

Em uma cidade do Canadá com climas frios na maioria das vezes, é necessário saber quando você pode sair 
sem precisar usar casacos, ou seja, quando há sol. Para isso, foi solicitado que você realizasse um programa 
que determina se as pessoas podem sair sem problemas, então apresentamos a função `input`.

'''


name = input("Write your name: ")

print(name)

hows_the_day = input('Write how is the day today: ')

if hows_the_day == 'sun':
    print('Você não precisa levar casaco')
else:
    print('Você precisa levar casaco')
## Como você pode ver com a função de entrada, podemos receber a entrada do teclado
## e armazená-los em variáveis.