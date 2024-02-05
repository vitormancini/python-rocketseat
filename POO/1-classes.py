class Pessoa:
    # Construtor sem retorno (None) que recebe parâmetros na instanciação da classe
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    # Método
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos"

# Objeto (instância da classe)
pessoa = Pessoa('Vitor', 29)

print(pessoa.nome) # Vitor
print(pessoa.idade) # 29
mensagem = pessoa.saudacao()
