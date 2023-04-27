# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

# Verifica o tipo do objeto que está dentro de determinada lista ou armazenado 
for item in lista:
    if isinstance(item, set):
        print('set')
        item.add(5)
        print(item,isinstance(item,set))
        
    # Para alterar a string, devemos entrar no valor e alterar diretamente la, como no exemplo abaixo      
    elif isinstance(item, str):
        print('String')
        print(item.upper())
        
    elif isinstance(item, (int, float)):
        print('Int ou Float')
        print(item, item * 2)
        
    else:
        print('Outro')
        print(item)