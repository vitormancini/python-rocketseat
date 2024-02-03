# Tuplas são coleções de elementos ordenáveis e imutáveis

frutas = ('banana', 'uva', 'maçã', 'pera', 'abacaxi')
#            0        1       2       3        4

print(type(frutas)) # <class 'tuple'>

elemento1 = frutas[0] # banana
elemento2 = frutas[1] # uva
elemento3 = frutas[2] # maçã
elemento4 = frutas[3] # pera
elemento5 = frutas[4] # abacaxi

# Retorna a quantidade de vezes que um elemento aparece na tupla
frutas.count('banana') # 1

# Retorna o indice do elemento especificado (lança uma exceção caso não exista o elemento)
index = frutas.index('uva') # 1