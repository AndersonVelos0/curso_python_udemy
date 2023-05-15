# Supomos que eu tenha qualquer dado e eu queira pega-lo depois
import json
# o JSON não suporta funções, etc, mas coisas vindas diretamente do python são suportadas
# basicamente o json serve para voce salvar dados fora do programa e puxa-los novamente 
pessoa = {
  "nome": "Luiz Otávio 2",
  "sobrenome": "Miranda",
  "enderecos": [
    {
      "rua": "R1",
      "numero": 32
    },
    {
      "rua": "R2",
      "numero": 55
    }
  ],
  "altura": 1.8,
  "numeros_preferidos": [
    2,
    4,
    6,
    8,
    10
  ],
  "dev": True,
  "nada": None
}

# # Salvando o arquivo
# with open('salvando_dados_json.json', 'w', encoding= 'utf8') as arquivo:
#     # dump faz um dump no arquivo
#     json.dump(pessoa,
#               arquivo, 
#               ensure_ascii= False, 
#               indent= 2)

# Escrevemos o json e importamos de volta o módulo 

with open('salvando_dados_json.json', 'r', encoding= 'utf8') as arquivo:
    # carregando uma string
    pessoa = json.load(arquivo)
    print(pessoa)
    print(pessoa['nome'])