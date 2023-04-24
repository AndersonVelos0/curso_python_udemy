# Métodos úteis:
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

# criando e adicionando
s1 = set()
s1.add('Luizin')
s1.add(1)

# atualizando o valor
s1.update(('Ola mundo!', 1,2,3,4))
print(s1)

# limpando o set 
# s1.clear()

# eliminando o valor passando o proprio valor
s1.discard('Ola mundo!')
print(s1)