class Personagem:
    def __init__(self, nome, vida, nivel):
        # Atributos privados
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    # geters e seters
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    @property
    def nivel(self):
        return self.__nivel
    
    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel
    
personagem = Personagem('Mario', '100', '1')
print(personagem.__nome) # Erro será lançado

