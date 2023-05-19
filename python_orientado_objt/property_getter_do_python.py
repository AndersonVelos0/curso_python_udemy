# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor 

    # Ele faz um método se comportar como atributo, não precisa dos parenteses pra chamar o método
    @property
    def cor(self):
        # Você pode alterar sem que quebre o código cliente, as pessoas utilizam como método, mas é um atributo
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 'Olá, mundo!'
    
# Pra o código cliente, será como se estivesse chamando um atributo, não uma função   
caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)


############################



# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor 
#     # Criado para proteger o atributo através do encapsulamento    
#     def get_cor(self):
#         print('Get cor:')
#         return self.cor_tinta    
        
# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

