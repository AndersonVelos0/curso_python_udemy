# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - mais rapidos que tuplas ou listas
# - são iteráveis (for, in, not in)
s1 = {1,2,2,2,2,2,2,2,2,2, 2, 3}  # com dados
print(s1)

# O set pode ser util para remover valores repetidos, tornando desnecessario o uso do for para ir removendo
l1 = [1,2,3,3,3,3,3,3,1,5]
s2= set(l1)
# Após converter de volta a lista, ele elimina os valores repetidos, contudo, pode não garantir a ordem
l1 = list(s2)
print(3 in s2)
print(l1)

for i in s2:
    print(i)
# Só aceitam valores imutaveis
