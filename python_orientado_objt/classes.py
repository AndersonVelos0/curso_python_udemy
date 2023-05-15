# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

# Exemplo, CRIAÇÃO DO MOLDE
class Pessoa:
    # O método init é o construtor, onde os parametros são passados
    def __init__(self, paramNome, paramSobrenome):
       self.nome = paramNome
       self.sobrenome = paramSobrenome 
    
# Criando o objeto pessoa 1
p1 = Pessoa('Anderson', 'Veloso')
print(p1.nome)
print(p1.sobrenome)