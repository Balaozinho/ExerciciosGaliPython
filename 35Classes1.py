#Ex 35. CADASTRO DE ALUNOS
#CRIE UMA CLASSE CHAMADA ALUNO COM OS SEGUINTES ATRIBUTOS: NOME, IDADE, CURSO
#E OS MÉTODOS: APRESENTAR () -> IMPRIME FRASE COMO "OLÁ, MEU NOME É ANA E ESTUDO EMPREENDEDORISMO" | ANIVERSARIO () -> ADICIONA 1 NA IDADE DO ALUNO


# Definindo a classe Aluno
class Aluno:
    # O método __init__ inicializa os atributos da classe
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    # Método que exibe informações sobre o aluno
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu estudo {self.curso}.")

    # Método que aumenta a idade do aluno em 1
    def aniversario(self):
        self.idade += 1
        print(f"Parabéns, {self.nome}! Agora você tem {self.idade} anos.")

# Criando alguns objetos da classe
aluno1 = Aluno("Ana", 15, "Empreendedorismo")
aluno2 = Aluno("Lucas", 14, "Tecnologia")
aluno3 = Aluno("Marina", 16, "Investimentos")

# Chamando os métodos
aluno1.apresentar()
aluno2.apresentar()
aluno3.apresentar()

aluno1.aniversario()
