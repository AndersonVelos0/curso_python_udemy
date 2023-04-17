# Ordem de precedencia, respectivamente

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

# Primeiro os parenteses de dentro são resolvidos
# Lembrando que o valor de uma variavel pode ser trocada enquanto o programa compila
# Pois ele lê da esquerda para direita, de cima para baixo
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)