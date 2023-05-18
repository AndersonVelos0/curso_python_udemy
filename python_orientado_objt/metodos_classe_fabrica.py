# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    
    # Criando o classmethods
    # É um método passado diretamente junto com a classe, sem passar O SELF (é um decorator)
    @classmethod
    def metodo_de_classe(self):
        print('Hey')
        
    # Criando um método da classe com cls, o molde
    # Já passamos o parametro de 50 anos 
    # Abaixo tem um factory method, que cria um novo objeto com alguma lógica qualquer
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    # Factory method para passar o nome e receber a idade
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)



p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()