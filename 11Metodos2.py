# Exercício 11 - CRIE UM SISTEMA DE GERENCIAMENTO DE CONVIDADOS
#PEÇA PARA O USUÁRIO ADICIONAR 3 NOMES EM UMA LISTA, UM DE CADA VEZ
#MOSTRE A LISTA DE CONVIDADOS EM TELA

#LOGO EM SEGUIDA, PEÇA PARA QUE O USUÁRIO REMOVA UM DOS CONVIDADOS
#VERIFIQUE SE ELE SE ENCONTRA NA LISTA E UTILIZE UM MÉTODO PARA REMOVÊ-LO
#NO FINAL, ORGANIZE A LISTA EM ORDEM ALFABÉTICA

convidados = []

for i in range(3):
    nome = input("Digite o nome do convidado: ")
    convidados.append(nome)

print("\nLista original:", convidados)

remover = input("Digite o nome de um convidado para remover: ")

if remover in convidados:
    convidados.remove(remover)

convidados.sort()
print("Lista atualizada e em ordem alfabética:", convidados)
