# Classe mãe (superclasse)
from abc import abstractmethod, ABC

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def saudacao(self):
        print(f'Ola, meu nome é {self.nome}')

    # Método abstrato (todos as classes filhas deverão implementar)
        @abstractmethod
        def bonificacao(self):
            pass

# Classe Professor que herda de Funcionario
class Professor(Funcionario):
    # Enviando parâmetros para o construtor da classe mãe
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def bonificacao(self):
        return self.salario * 0.1

professor = Professor('Vitor', 4350.24)
professor.saudacao()
bonificacao = professor.bonificacao()
print(bonificacao) # 435.024
