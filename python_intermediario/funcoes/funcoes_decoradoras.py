# Funções decoradoras e decoradores
# significa efetuar isso em funções Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Esse procedimento deve ser feito com o closure


# Criando a função decoradora
def criar_funcao(func):
    # Criando uma função interna para que os argumentos sejam guardados sem executar
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi: {resultado}.')
        print('Ok, você foi decorada')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        # Renomeando o erro
        raise TypeError('Param deve ser um valor do tipo String(str)')


inverte_string_checando_param = criar_funcao(inverte_string)
invertida = inverte_string_checando_param('Anderson')
print(invertida)
