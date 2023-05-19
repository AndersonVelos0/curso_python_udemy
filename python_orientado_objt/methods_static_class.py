# method vs @classmethod vs @staticmethod
# method - self, método de instância (tem acesso a tudo, recebe a instancia)
# @classmethod - cls, método de classe (recebe a propria classe no parametro)
# @staticmethod - método estático (❌self, ❌cls)

class Conection:
    # metodo de instancia para iniciar os valores de atributos da instancia
    def __init__(self, host = 'localhost'):
        self.host = host 
        self.user = None
        self.password = None
        
    
    # metodo setter para o user 
    def set_user(self, user):
        self.user = user
        
     # TODAS AS VEZES QUE O SELF FOR UTILIZADO, ESSE MÉTODO É UM MÉTODO DE INSTANCIA
    def set_password(self, password):
        self.password = password 
       
    
    # Suponha que eu queira criar um metodo que já recebe o user e senha
    @classmethod
    def create_with_auth(cls, user, password):
        # criando uma variavel do metodo
        connection = cls()
        # é parecido com o self, porem, diretamente da classe
        connection.user = user
        connection.password = password
        return connection
        
    @staticmethod
    def log(msg):
        print('Log:', msg)
        
        
# c1 = Conection()
c1 = Conection.create_with_auth('XzubimaruX','1212423')
# c1.set_user('Anderson')
# c1.set_password('Anderson')
print(Conection.log('Essa é a mensagem de log'))
print(c1.user)        
print(c1.password)        

