# Exercício 19 - SISTEMA DE CADASTRO

#CRIE UM SISTEMA DE CADASTRO DE NOMES DE ALUNOS
#PEÇA PARA O USUÁRIO INFORMAR A QUANTIDADE DE NOMES QUE ELE QUER CADASTRAR
#LOGO EM SEGUIDA, ADICIONE ESSES NOMES EM UMA LISTA E MOSTRE O RESULTADO EM TELA DE TODOS OS ALUNOS

alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    alunos.append(nome)

print("\nLista de alunos:", alunos)
