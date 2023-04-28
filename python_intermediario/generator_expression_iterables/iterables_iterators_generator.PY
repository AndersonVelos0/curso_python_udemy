# Generator Expression , Iterables e Iterators em Python 

# O iterator é responsável por descobrir apenas o proximo valor do seu iteravel
# para te entregar um valor por vez

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # Tem __iter__ e __next__

# o iterator esgota os valores, ao fim, todos serão consumidos
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))