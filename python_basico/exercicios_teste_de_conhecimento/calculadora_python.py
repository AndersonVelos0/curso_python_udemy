# Calculadora com While

while True:
    
    numero1 = input('Digite um numero: ')
    numero2 = input('Digite outro numero: ')
    operador = input('Digite o operador: (+ - / * ): ')
    
    # Criando uma flag de verificação 
    numero1_float = 0
    numero2_float = 0
    numeros_validos = None   
    # Contornando possiveis erros / má pratica
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
        
    except:
        numeros_validos = None

    # Se os numeros forem None, entrará na except e em seguida entrada no if abaixo
    # o if abaixo irá retornar ao laço
    if numeros_validos is None:
        print('Um ou ambos os numeros digitados são invalidos')
        continue
        
    operadores_permitidos = '+ - / * '  
    
    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue
    
    if len(operador) > 1:
        print('Operador invalido')
        continue
       
    # Operações
    print('Realizando sua conta. Confira o resultado abaixo:')
    
    if operador == '+':
        print(numero1_float + numero2_float)
    
    elif operador == '-':
        print(numero1_float - numero2_float)
    
    elif operador == '/':
        print(numero1_float / numero2_float)
        
    elif operador == '*':    
        print(numero1_float * numero2_float)
     
    else: 
        print('Nunca deveria chegar aqui!!')   
    # sair em lowercase e verificando se começa com s
    sair = input('Quer sair? [s]im: ').lower().startswith('s' or 'S')
    print(sair)                                       
    
    if sair is True:
        break