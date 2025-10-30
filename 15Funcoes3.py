# Exercício 15
#CRIE UM SISTEMA DE NOTAS QUE CONTENHA 3 FUNÇÕES
#FUNÇÃO COLETAR NOTAS, ONDE RECEBA COMO PARAMETRO A QUANTIDADE DE NOTAS A SER LANÇADA E POSTERIORMENTE, ARMAZENADA EM UMA LISTA
#FUNÇÃO CALCULAR MÉDIA, ONDE RECEBA COMO PARAMETRO A LISTA DE NOTAS ADICIONAS E RETORNE A MÉDIA DELA
#FUNÇÃO AVALIAR TURMA, ONDE RECEBA A MÉDIA CALCULADA E VERIFICA SE ELA É MAIOR OU IGUAL A 7 
#UTILIZE TODAS AS FUNÇÕES E MOSTRE O RESULTADO EM TELA

def coletar_notas(qtd):
    notas = []
    for i in range(qtd):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        notas.append(nota)
    return notas

def calcular_media(lista):
    return sum(lista) / len(lista)

def avaliar_turma(media):
    if media >= 7:
        print("Turma com bom desempenho!")
    else:
        print("Turma precisa melhorar!")

# Programa principal
quantidade = int(input("Quantos alunos há na turma? "))
notas_turma = coletar_notas(quantidade)
media_turma = calcular_media(notas_turma)

print("\nMédia da turma:", media_turma)
avaliar_turma(media_turma)
