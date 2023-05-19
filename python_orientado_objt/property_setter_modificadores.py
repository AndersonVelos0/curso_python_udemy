# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯



class Caneta:
    def __init__(self, cor): 
        # quando tem um underline antes do atributo, ele não deve ser usado
        # em python isso é semelhante a um private ou protected 
        self._cor = cor
        self._cor_tampa = None

    # Ele faz um método se comportar como atributo, não precisa dos parenteses pra chamar o método
    @property
    def cor(self):
        # Você pode alterar sem que quebre o código cliente, as pessoas utilizam como método, mas é um atributo
        print('PROPERTY')
        return self._cor
     
    # O setter serve para limitar o usuário nas coisas que você não quer que ele insira no código 
    # tem que ter o self e receber um valor
    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
           raise ValueError('Não aceito essa cor') 
        self._cor = valor


    @property
    def cor_tampa(self):
        return self._cor_tampa 
    
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor
        

        
# Pra o código cliente, será como se estivesse chamando um atributo, não uma função   
caneta = Caneta('Azul')
caneta.cor = 'Azul'
caneta.cor_tampa = 'Preto'
print(caneta.cor)
print(caneta.cor_tampa)


# getter serve para obter o valor, chamá-lo
# setter serve para 