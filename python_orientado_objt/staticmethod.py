# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Pessoa:
    # Criando um método estatico, é uma função dentro da classe, não tem acesso a nada
    # ele apenas está dentro da classe
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('oi', args, kwargs)
        
        
def funcao(*args, **kwargs):
    print('oi', args, kwargs)
    
    
c1 = Pessoa()
c1.funcao_que_esta_na_classe()
funcao(1,2,3)
Pessoa.funcao_que_esta_na_classe(nomeado = 1 )
funcao(nomeado = 1)