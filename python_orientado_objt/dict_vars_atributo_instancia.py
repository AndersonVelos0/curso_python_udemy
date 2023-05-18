# __dict__ e vars para atributos de instância
# Eles mantem um objeto do tipo dicionario dentro do objeto final
class Pessoa:
    ano_atual = 2022
    #É um atributo 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

# DICT seria utilizado para salvar os dados caso precise de um dicionario
dados = {'nome': 'João', 'idade': 35}
# Quando desempacota um dicionario, você cria a chave igual o valor
p1 = Pessoa(**dados)
# p1.nome = 'EITA'
# print(p1.idade)
# É uma função para salvar e editar dados em dicionario
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
# Vars 
print(vars(p1))
print(p1.nome)