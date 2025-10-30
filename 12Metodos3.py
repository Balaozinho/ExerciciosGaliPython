# Exercício 12 - CALCULADORA DE MÉDIAS
#PEÇA PARA QUE O USUÁRIO LANCE 5 NOTAS DIFERENTES E AS ADICIONE EM UMA LISTA
#CALCULE A MÉDIA UTILIZANDO MÉTODOS DE SUM() E LEN()
#MOSTRE O RESULTADO EM TELA

notas = []

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("\nNotas da turma:", notas)
print("Média da turma:", media)
print("Maior nota:", max(notas))
print("Menor nota:", min(notas))
