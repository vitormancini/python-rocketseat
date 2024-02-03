# Função sem retorno
def saudacao(nome):
    print(f'Ola {nome}!')

# Chamando a função
saudacao('Vitor')

# Função com retorno
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

# Chamando a função
resultado = soma(5, 2)

# Parâmetro opcional (se não enviar, assumirá um valor predefinido)
def subtracao(n1, n2 = 10):
    return n1 - n2

resultado = subtracao(20)