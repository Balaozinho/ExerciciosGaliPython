# Exercício 3 - PEÇA PARA O USUÁRIO INFORMAR UMA NOTA E FREQUENCIA DE UM ALUNO
#CONFIGURE REQUISITOS DE APROVAÇÃO, ASSUMINDO NOTA MAIOR OU IGUAL A 7 E FREQ MAIOR QUE 75%
#O ALUNO SÓ SERÁ APROVADO CASO ATENDAS OS DOIS CRITÉRIOS, MOSTRE O RESULTADO UTILIZANDO PRINT

nota = float(input("Digite a nota do aluno: "))
frequencia = float(input("Digite a frequência (%): "))

atingiu_nota = nota >= 7
atingiu_frequencia = frequencia >= 75
aprovado = atingiu_nota and atingiu_frequencia

print("Atingiu nota mínima?", atingiu_nota)
print("Atingiu frequência mínima?", atingiu_frequencia)
print("O aluno foi aprovado?", aprovado)
