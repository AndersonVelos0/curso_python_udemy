# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código

class Carro:
    # Metodo init sempre retorna NONE 
    def __init__(self, nome):
        self.nome = nome # Hard coded
        
    
    # um método é uma função que está dentro da classe fazendo algo
    def acelerar(self):
        print(f'{self.nome} está acelerando')
    
carro1 = Carro('Fusquinha')
print(carro1.nome)
carro1.acelerar()

carro2 = Carro('Gol quadrado')
print(carro2.nome)
carro2.acelerar()