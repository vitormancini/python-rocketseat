# Dicionario é uma coleção não ordenada de chave e valor

pessoa = {
    'nome': 'Vítor', 
    'idade': 29, 
    'admin': True
}

print(type(pessoa)) # <class 'dict'>

pessoa['nome'] # Vítor
pessoa['idade'] # 29
pessoa['admin'] # True

# Criando novas chaves para o dicionario
pessoa['sobrenome'] = 'Mancini'

# Remove uma chave
del pessoa['sobrenome']

# Retorna as chaves do dicionario em formato de lista
chaves = list(pessoa.keys()) # ['nome', 'idade', 'admin']

# Retorna os valores do dicionario em formato de lista
valores = list(pessoa.values()) # ['Vítor', 29, True]

# Retorna uma lista de tuplas, onde cada elemento é chave/valor
items = list(pessoa.items()) # [('nome', 'Vítor'), ('idade', 29), ('admin', True)]

items[0][0] # nome
items[0][1] # Vítor