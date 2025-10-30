# Exercício 17 - CONTADOR DE PALAVRAS E LETRAS
#PEÇA PARA O USUÁRIO DIGITAR UMA FRASE
#UTILIZE DE MÉTODOS E FUNÇÕES PARA CONTAR O NÚMERO DE PALAVRAS E LETRAS
#MOSTRE O RESULTADO EM TELA DE (1) PALAVRAS, (2) LETRAS E (3) OCORRENCIAS DA LETRA A

frase = input("Digite uma frase: ").strip().lower()

palavras = frase.split()
qtd_palavras = len(palavras)

letras_sem_espaco = len(frase.replace(" ", ""))
ocorrencias_a = frase.count("a")

print("Palavras:", qtd_palavras)
print("Letras (sem espaços):", letras_sem_espaco)
print("Ocorrências da letra 'a':", ocorrencias_a)
