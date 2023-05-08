# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.


# Decoradores são "Syntax Sugar" (Açúcar sintático)  @syntax_sugar
# Python tem funcionalidades que facilitam o uso das funções decoradoras
# Sem que seja necessário rescrita de código 

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


# Utilizando o decorador com o syntax_sugar 
@criar_funcao
# a partir de agora, a função inverte_string não será mais ela, será substituida pela interna()
def inverte_string(string):
    # verificando o nome
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        # Renomeando o erro
        raise TypeError('Param deve ser um valor do tipo String(str)')

invertida = inverte_string('123')
print(invertida)

# Resumidamente, funções decoradoras servem para receber outra função, onde uma função interna é criada
# de modo que você possa Adicionar / Remover/ Restringir / Alterar os dados, sem que essa função original
# seja chamada, através do closure, quando você chamá-la, vai estar fechada. 

# No caso do syntex_sugar ele é utilizado para que você não precise rescrever a chamada da função, somente passando o @função_decoradora