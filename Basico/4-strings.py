nome = 'Vitor'
sobrenome = 'Mancini'

# %s
print('Meu nome é %s %s' %(nome, sobrenome))

# Format
print('Meu nome é {} {}'.format(nome, sobrenome))

# Converte string para maiúscula
nome_maiusculo = nome.upper() # VITOR

# Converte string para minúscola
nome_minusculo = nome.lower()

# IMPORTANTE: as strings são imutáveis, uma vez declarada seu valor, não é possível mais alterar

# Quantidade de letras
len(nome) # 5

# Buscando letras
primeira_letra = nome[0] # V
segunda_letra = nome[1] # i

# Quantidade de ocorrências em uma string
nome.count('i') # 1

# retorna o index da primeira ocorrência (retorna -1 caso não encontre)
nome.find('a') # -1

# Converte a string para byte
bytes = nome.encode() # b'Vitor'

# Converte bytes para string
decode = bytes.decode() # Vitor

# Substitui uma ocorrência por outra
nome.replace('i', 'a') # Vator

# Adiciona um separador a qualquer variavel iterável
'-'.join(nome) # V-i-t-o-r

# Transforma em uma lista através de um caratcer específico
nome_completo = 'Vitor Mancini Rodrigues'
nome_completo.split(' ') # ['Vitor', 'Mancini', 'Rodrigues']

# Remove um caractere específico do começo e final de uma string
nome_completo.strip('V') # itor Mancini Rodrigues

# Verifica se string começa com (retorna um booleano)
nome.startswith('Vi') # True

# Veirifica se termo existe na string (retorna booleano)
'tor' in nome # True

# Veirifica se termo não existe na string (retorna booleano)
'abc' not in nome # True