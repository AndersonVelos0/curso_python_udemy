# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))




def generator(n=0, maximum=10):
    while True:
        # É utilizado em geradores com a palavra yield, que tem a funcionalidade do return
        # Ele pausa a execução da função e guarda o ultimo valor, podendo chamar o next
        # todo generator é um iterator
        yield n
        n += 1
        
        if n >= maximum:
            return 

gen = generator(maximum=1000000)
for n in gen:
    print(n)
    


# gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))