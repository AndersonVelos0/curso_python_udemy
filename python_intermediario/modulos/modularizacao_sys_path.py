# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes na mesma pasta
# nos caminhos de sys.path

# import sys

# Está importando o módulo da aula no pacote módulo
import aula97_m
# importando especificamente
from aula97_m import testando_importacao

print(aula97_m.testando_importacao)
print(testando_importacao)
# Verificando o nome do módulo
print('Este módulo se chama', __name__)
# print(sys.path, sep = '\n')
