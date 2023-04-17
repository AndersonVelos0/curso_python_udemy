'''

O que faremos é implementar uma versão básica do jogo na próxima célula. 
Você receberá duas entradas que serão **player_1** e **player_2** nessa ordem, por enquanto, 
considere que você só pode inserir uma das opções válidas listadas acima, 
imprima quem ganhou com base nas regras e usando as condicionais que já aprendemos.

'''


player_1 = input("Write the value chosen by player 1: ")
player_2 = input("Write the value chosen by player 2: ")

# Verifica se as entradas são válidas
valid_inputs = ["pedra", "papel", "tesoura", "lagarto", "spock"]
if player_1 not in valid_inputs or player_2 not in valid_inputs:
    print("Entrada inválida, as opções válidas são:", valid_inputs)
else:
    # Define as regras do jogo
    rules = {
        "pedra": ["tesoura", "lagarto"],
        "papel": ["pedra", "spock"],
        "tesoura": ["papel", "lagarto"],
        "lagarto": ["papel", "spock"],
        "spock": ["pedra", "tesoura"]
    }

    # Verifica quem ganhou
    if player_1 == player_2:
        print("Empate!")
    elif player_2 in rules[player_1]:
        print("Jogador 1 ganhou!")
    else:
        print("Jogador 2 ganhou!")