
# Serve para recarregar o módulo em python, ele não sera singleton (não carregará apenas uma vez e pronto)
import importlib

# sSomente importado, ele não irá recarregar, tera apenas um uso, quando chamado
import aula98_m

print(aula98_m.variavel)

for i in range(10):
    # Cada vez que ele tiver em reload, ele irá recarregar todas as vezes
    importlib.reload(aula98_m)
    print(i)

print('Fim')