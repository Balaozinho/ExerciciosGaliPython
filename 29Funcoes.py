#EXERCICIO 29 - CALCULANDO MÉDIA DE ALUNOS

#CRIE UM SISTEMA QUE CALCULA MÉDIA DE ALUNOS
#FAÇA UMA FUNÇÃO CHAMADA CALCULAR_MEDIA E QUE RECEBA COMO PARÂMETRO UMA LISTA DE NOTAS DE ALUNOS, RETORNANDO UMA MÉDIA PARA CADA ALUNO
#CRIE UMA FUNÇÃO CHAMADA AVALIAR_ALUNO E QUE RECEBA O NOME E NOTA MÉDIA DO ALUNO COMO PARÂMETRO
#RETORNE MENSAGENS DIFERENTES PARA CADA INTERVALO
# 9 A 10 - PARABÉNS!
# 7 - 8.9 - MUITO BEM!
# 5 - 6.9 - ATENÇÃO! SE DEDIQUE MAIS
# ABAIXO DE 5 - DEU RUIM!

notas = []

def calcular_media(lista_notas):
    media = sum(notas) / len(notas)
    return media

qtdade_notas = int(input("Quantas notas você quer lançar? "))

for n in range(1, qtdade_notas+1):
    nota = float(input(f"Digite a nota {n}: "))
    notas.append(nota)

media_notas = calcular_media(notas)

def avaliar_notas(media_notas):
    if media_notas >=9 and media_notas <= 10:
        print(f"Parabéns! Sua média é {media_notas}")
    elif media_notas >=7 and media_notas <= 8.9:
        print(f"Muito bem! Sua média é {media_notas}")
    elif media_notas >=5 and media_notas <= 6.9:
        print(f"Atenção, se dedique mais! Sua média é {media_notas}")
    elif media_notas >=0 and media_notas <= 4.9:
        print(f"Deu ruim! Sua média é {media_notas}")
    else:
        print("ERRO - Sua média não está no intervalo de 1 a 10!")

avaliar_notas(media_notas)