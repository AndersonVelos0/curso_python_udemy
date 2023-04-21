'''
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de inserir, apagar e listar os valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista

'''


lista_de_compras = []

while True:
    print('Selecione uma opção para prosseguir: ')
    opcao = input('[i]nserir [a]pagar [l]istar:')

    if opcao == 'i':
        valor = input('Qual valor você deseja adicionar?')
        lista_de_compras.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha um valor para deletar')

        # Utilizando de forma rude o try except para contornar possiveis quebras
        try:
            indice = int(indice_str)
            del lista_de_compras[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        if len(lista_de_compras) == 0:
             print('Não há nada para deletar em sua lista!')

        for i, valor in enumerate(lista_de_compras):
            print(i, valor)
    
    else:
        print('Opção invalida! Opções disponíveis: i / a / l')
        break

