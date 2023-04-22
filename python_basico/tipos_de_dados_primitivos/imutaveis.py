"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'a1000'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
print(string.capitalize())

# Permite que a variavel nunca seja truncada
print(string.zfill(10))

# Esses são os métodos do Python que funcionam em string, agora vamos ver os métodos específicos de string.

# capitalize() -> Coloca a 1ª letra Maiúscula;
# casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente);
# count() -> Conta a quantidade de vezes que um valor/símbolo/letra aparece na string;
# find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado (lá no início falamos que cada letra/símbolo tem uma posição no texto);
# format() -> Formata uma string de acordo com os valores passados;
# isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou ç são considerados letras para essa função;
# isalpha() -> Verifica se um texto é todo feito de letras;
# isnumeric() -> Verifica se um texto é todo feito por números;
# replace() -> Substitui um texto por um outro texto em uma string;
# split() -> Separa uma string de acordo com um delimitador em vários textos diferentes;
# splitlines() -> separa um texto em vários textos de acordo com os “enters” do texto;
# startswith() -> Verifica se a string começa com determinado texto;
# strip() -> Retira caracteres indesejados dos textos. Por padrão, retira espaços “extras” no início e no final;
# title() -> Coloca a 1ª letra de cada palavra em maiúscula;
# upper() -> Coloca o texto todo em letra maiúscula.