# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# É uma biblioteca (MÓDULO)  para copiar profundamente os dados dos dicionarios
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'lista': [1,2,3,4]    
}

# Utilizando uma shallow copy sem que um interfira no outro com copia raza (copia tudo imutavel)
# Contudo, se houverem valores mutaveis dentro do dicionario, ele vai fazer os dois dicionarios apontarem para o mesmo valor
d2 = d1.copy()
# Uma deepcopy é igual ao copy
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2 ['lista'][0] = 100000
# acima o valor foi alterado nas duas listas
print(d1)
print(d2)



