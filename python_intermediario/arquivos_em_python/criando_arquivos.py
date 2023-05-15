# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# Caso você não passe o caminho completo, o python criará o arquivo na pasta em que está
caminho_arquivo = 'C:\\Users\\Anderson\\Documents\\curso_python_udemy\\python_intermediario\\arquivos_em_python\\Nova pasta Atenção\\'
caminho_arquivo += 'criando_arquivos.txt'

# Criando arquivo com comandos, passamos o nome e o comando 
# arquivo = open(caminho_arquivo, 'w')
# # Quando abrir, feche sempre o arquivo
# arquivo.close()

# Utilizando o context manager
with open(caminho_arquivo, 'w+') as arquivo:
    # print('olá mundo!')
    # print('Arquivo será fechado!')
    arquivo.write('Linha 1 do arquivo\n')
    arquivo.write('Linha 2 do arquivo\n')
    # escrevendo varias linhas com writelines
    arquivo.writelines(('Linha 3\n','Linha 4\n'))
    # a função seek move o cursor para cima antes da quebra de linha
    arquivo.seek(0,0)
    arquivo.read()
    # lendo todos os arquivos de uma vez
    print('Lendo')
    arquivo.seek(0,0)
    print(arquivo.readline(), end = '')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    
    print('Readlines')
    arquivo.seek(0,0)
    # lendo com readlinesss
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 10)
    
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
