# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos, onde um atributo liga à um objeto da outra classe
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.



class Escritor:
    def __init__(self, nome):
        self.nome = nome
        # através do atributo protected ferramenta, acessamos a outra classe
        self._ferramenta = None

    # o property está fazendo um getter
    @property
    def ferramenta(self):
        return self._ferramenta
    # setter para alterar
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())