for i in range(10):
    # se for 2, irá pular o 2 e irá continuar, irá voltar para o começo
    if i == 2:
        print('i é 2, pulando...')
        continue
    # Quando i for 8, ele dará break
    if i == 8:
        print('i é 8, seu else não executará')
        break
    # iniciará no 1 e terminará no 2, o for será quebrado
    # primeiro irá passar os dois primeiros ifs e virá iterar com j
    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')
