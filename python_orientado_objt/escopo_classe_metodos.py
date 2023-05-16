# Escopo da classe e de métodos da classe
class Animal:
    # Atributo de classe
    # nome = 'Leão'

    # Atributos de instancia utilizam a palavra self
    def __init__(self, nome):
        self.nome = nome
        # Escopo do init, variavel definida dentro de um metodo
        # Não pode ser chamada dentro de outro a n ser com o uso do self
        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):
        # Irá permitir por conta do uso do self, função terá seu namespace dentro dela
        return self.comendo(*args, **kwargs)



leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))