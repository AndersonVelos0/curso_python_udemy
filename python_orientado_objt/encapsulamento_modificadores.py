# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.


# Python não tem modificadores de acesso, porém, podemos usar convenção para simular

from functools import partial

class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        # criando um atributo protected (CLASSE E SUBCLASSE)
        self._protegido = 'Isso é protegido'
        # criando um atributo private (CLASSE) 
        self.__privado = 'Isso é privado'
        
        
    def metodo_publico(self):
        self._metodo_protected()
        return 'metodo publico'
    
    # criado para uso interno da classe utilizando logica interna
    def _metodo_protected(self):
        return 'metodo protegido'
    # criando um metodo privado
    def __metodo_private(self):
        print('metodo_private')
        return 'metodo_private'

f = Foo()
print(f.public)
print(f.metodo_publico())