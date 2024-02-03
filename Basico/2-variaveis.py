# Tipo texto
nome = 'Vitor Mancini'
print(f'{nome} - {type(nome)}') # Vitor Mancini-<class 'str'>

# Tipo numérico inteiro
idade = 29
print(idade, type(idade), sep='-') # 29-<class 'int'>

# Tipo numérico decimal
peso = 89.5
print({peso}, type(peso), sep='-') # 89.5-<class 'float'>

# Tipo booleano
maior_de_idade = True
print(maior_de_idade, type(maior_de_idade), sep='-') # True-<class 'bool'>

# f-strings: podemos concatenar varíaveis com textos dentro do comando print
# sep: define qual será o separador dentro do comando print (o padrão é uma espaço vazio)
# end: define qual ocorrerá no final do comando print (por padrão é o \n - quebra de linha)

