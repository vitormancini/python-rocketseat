class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return f'{self.nome} está emitindo som...'

# Classe filha
class Mamifero(Animal):
    def amamentar(self):
        return f'{self.nome} está amamentando...'
    
# Classe filha
class Ave(Animal):
    def voar(self):
        return f'{self.nome} está voando...'
    
# Classe filha 
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return super().emitir_som() # Chama o método da classe mãe
        
morcego = Morcego('Morcego')
print(morcego.emitir_som())
print(morcego.amamentar())
print(morcego.voar())