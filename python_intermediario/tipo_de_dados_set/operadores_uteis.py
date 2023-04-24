# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


s2 = {1, 2, 3}
s3 = {2, 3, 4}
# Retorna a uniao dos dois conjuntos
s4 = s2 | s3
# Retorna os itens presentes em ambos os sets
s4 = s2 & s3
# A diferença retorna apenas os itens no set da esquerda, tem de ser posto em ordem
s4 = s2 - s3
# Diferença simetrica retorna os itens que não estão presentes em ambos, sao unicos
s4 = s2 ^ s3
print(s4)