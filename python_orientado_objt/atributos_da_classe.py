# Atributos da Classe

class Pessoa:
    # Atributo da classe pode usar em qualquer lugar
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        
    def get_ano_nascimento(self):
        # Pegando o atributo da classe
        # Utilizando o nome da classe, não há transtorno
        return Pessoa.ano_atual - self.idade
    
    
p1 = Pessoa('Anderson', 23)
p2 = Pessoa('Beatris', 22)

print(Pessoa.ano_atual)
# Voce alterando o valor, altera as contas
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
