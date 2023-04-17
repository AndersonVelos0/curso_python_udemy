# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool


# Está convertendo string para int
print(int('1'), type(int('1')))
# Está convertendo uma string para float
print(type(float('1') + 1))
# Está convertendo uma string para boolean, uma string que tenha um espaço é true
print(bool(' '))
# Está convertendo um int para string e concatenando com outra string 
print(str(11) + 'b')    