# for
nome = 'Vítor'

for letra in nome:
    print(letra, end='-') # V-í-t-o-r-

lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento, end=',') # 1,2,3,4,5,

dicionario = { 
    'nome': 'Vitor',
    'sobrenome': 'Mancini',
    'idade': 29
}

for chave in dicionario.keys():
    print(chave, end=',') # nome,sobrenome,idade,

for valor in dicionario.values():
    print(valor, end=',') # Vitor,Mancini,29,

for chave,valor in dicionario.items():
    print('%s - %s' %(chave, valor), end=",") # nome - Vitor,sobrenome - Mancini,idade - 29,

# Intervalo numérico
for i in range(1,11):
    print(i, end='-') # 1-2-3-4-5-6-7-8-9-10-

# indice e valor
for indice, valor in enumerate(lista):
    print(indice, valor, sep=',', end='-') # 0,1-1,2-2,3-3,4-4,5-

# WHILE
    
contador = 0
while contador < 10:
    print(contador, end='-') #0-1-2-3-4-5-6-7-8-9-
    contador += 1