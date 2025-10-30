# Exercício 16 - FORMATANDO O NOME
#PEÇA PARA O USUÁRIO INFORMAR O NOME COMPLETO
#IMPRIMA ESSE NOME TRATANDO-O E COLOCANDO A PRIMEIRA LETRA DE CADA PALAVRA EM MAIUSCULA
#IMPRIMA ESSE NOME TRATANDO-O E COLOCANDO TODAS AS LETRAS EM MAIUSCULA
#CONTE AS LETRAS SEM CONDERACAO OS ESPAÇOS E IMPRIMA EM TELA O RESULTADO

nome = input("Digite seu nome completo: ").strip()

print("Nome formatado:", nome.title())
print("Em maiúsculas:", nome.upper())

# Conta letras sem os espaços
letras = len(nome.replace(" ", ""))
print("Total de letras:", letras)
