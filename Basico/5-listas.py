# Listas são coleções de elementos ordenáveis e mutáveis
nomes = ['Vitor', 'Lucas', 'João', 'Maria', 'Matheus']
#          0         1        2       3         4

print(type(nomes)) # <class 'list'>

# Quantidade elementos
len(nomes) # 5

elemento1 = nomes[0] #Vitor
elemento2 = nomes[1] #Lucas
elemento3 = nomes[2] #João
elemento4 = nomes[3] #Maria
elemento5 = nomes[4] #Matheus

# Obtem uma quantidade específica de elementos (início, quantidade)
nomes[0:3] # ['Vitor', 'Lucas', 'João']

# Do primeiro elemento, obter 2 => nomes[:2]
# Do ultimo elemento, obter 3 => [3:
# Obter o ultimo elemento => nomes[-1]

# Adiciona um elemento no final da lista
nomes.append('Taynara') # ['Vitor', 'Lucas', 'João', 'Maria', 'Matheus', 'Taynara']

# Insere um elemento em um indice específico
nomes.insert(1, 'Gustavo') # ['Vitor', 'Gustavo', 'Lucas', 'João', 'Maria', 'Matheus', 'Taynara']

# Retorna o indice do elemento especificado (lança uma exceção caso não exista o elemento)
index = nomes.index('Maria') # 3

# Remove e retorna o elemento de um indice
nomes.pop(3) # Remove e retorna João

# Remove um elemento
nomes.remove('Gustavo')

# Ordena a lista (deve possuir apenas um tipo de elemento)
nomes.sort() # ['Lucas', 'Maria', 'Matheus', 'Taynara', 'Vitor']

