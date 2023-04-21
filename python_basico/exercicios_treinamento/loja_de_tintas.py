'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''

# metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

# litros_necessarios = metros_quadrados / 3
# latas_necessarias = float(litros_necessarios / 18) + (litros_necessarios % 18 > 0)
# preco_total = latas_necessarias * 80

# print(f"Quantidade de latas de tinta: {latas_necessarias: .2f}")
# print(f"Preço total: R$ {preco_total:.2f}")


class CustomList:
    def __init__(self, items):
        self.items = items
    
    def get(self, index):
        if index < len(self.items):
            return self.items[index]
        else:
            print("O índice que você está tentando acessar não está na lista")
            return None

custom_list = CustomList([1, 2, 3, 4, 5])

## Deve retornar o valor 3
print(custom_list.get(2))
## Deve imprimir a mensagem
print(custom_list.get(90))
