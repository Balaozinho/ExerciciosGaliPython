# Exercício 18 - CENSOR DE PALAVRAS PROIBIDAS
#PEÇA PARA O USUÁRIO DIGITAR UMA FRASE
#PEÇA PARA O USUÁRIO DIGITAR QUAIS PALAVRAS SÃO PROIBIDAS E QUE AS SEPARE EM VIRGULAS
#TRATE AS PALAVRAS UTILIZANDO OS MÉTODOS NECESSÁRIOS
#PERCORRA A LISTA DE PALAVRAS PROIBIDAS E AS SUBSTITUA COM ****
#MOSTRE O TEXTO CENSURADO

frase = input("Digite uma frase: ").lower()
proibidas = input("Palavras proibidas (separadas por vírgula): ").lower().split(",")

# Remove espaços extras das palavras proibidas
proibidas = [p.strip() for p in proibidas]

for palavra in proibidas:
    frase = frase.replace(palavra, "***")

print("\nTexto censurado:", frase)
