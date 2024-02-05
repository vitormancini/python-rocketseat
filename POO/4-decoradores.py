def meu_decorador(func):
    def wrapper():
        print('Antes da função ser chamada...')
        func()
        print('Depois da função ser chamada...')
    return wrapper

@meu_decorador
def minha_funcao():
    print('Minha função foi chamada!')

minha_funcao()

""" Antes da função ser chamada...
Minha função foi chamada!
Depois da função ser chamada... """

class MeuDecoradorClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('Antes da função ser chamada...')
        self.func()
        print('Depois da função ser chamada...')

@MeuDecoradorClasse
def segunda_funcao():
    print('Minha segunda função foi chamada!')

segunda_funcao()

""" Antes da função ser chamada...
Minha segunda função foi chamada!
Depois da função ser chamada... """

# -----------------------------------------------------------------

# DECORADORES MAIS COMUNS

class MinhaClasse:

    valor = 10 # Atrbuto de classe

    def __init__(self, nome):
        self.nome = nome # Atributo de instância

    def metodo_instancia(self):
        return f'Método de instância chamado {self.nome}!'
    
    @classmethod # (possui acesso aos atributos de classe)
    def metodo_classe(cls):
        return f'Método de classe chamado {cls.valor}!'
    
    @staticmethod # (Náo possui acesso a nenhum atributo)
    def metodo_estatico():
        return f'Método estático chamado!'
    
obj = MinhaClasse('Vitor')
print(obj.metodo_instancia()) # Método de instância
print(MinhaClasse.metodo_classe()) # Método de classe
print(MinhaClasse.metodo_estatico()) # Método estático
