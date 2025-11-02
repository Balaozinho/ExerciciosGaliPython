#EX. 36 SISTEMA DE FUNCIONARIOS
#CRIE UMA CLASSE FUNCIONARIO COM ATRIBUTOS: NOME, SALARIO | MÉTODO: MOSTRAR_INFOS () -> EXIBE O NOME E SALÁRIO DO COLABORADOR
#CRIE DUAS SUBCLASSES. 1. GERENTE -> QUE TEM BONUS DE 20% NO SALARIO E 2. VENDEDOR -> BÔNUS DE 10% NO SALÁRIO
#AS DUAS CLASSES DEVEM SOBRESCREVER O MÉTODO MOSTRAR_INFOS() PARA INCLUIR O SALÁRIO COM BÔNUS APLICADO

# Classe base
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome} | Salário base: R$ {self.salario:.2f}")

# Subclasse Gerente
class Gerente(Funcionario):
    def mostrar_informacoes(self):
        salario_com_bonus = self.salario * 1.20  # bônus de 20%
        print(f"Nome: {self.nome} | Cargo: Gerente | Salário com bônus: R$ {salario_com_bonus:.2f}")

# Subclasse Vendedor
class Vendedor(Funcionario):
    def mostrar_informacoes(self):
        salario_com_bonus = self.salario * 1.10  # bônus de 10%
        print(f"Nome: {self.nome} | Cargo: Vendedor | Salário com bônus: R$ {salario_com_bonus:.2f}")

# Criando objetos
func1 = Gerente("Carlos", 5000)
func2 = Vendedor("Julia", 3000)

# Chamando o mesmo método em objetos diferentes
func1.mostrar_informacoes()
func2.mostrar_informacoes()
