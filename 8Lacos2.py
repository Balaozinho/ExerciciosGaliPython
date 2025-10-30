# Exercício 7 - FAÇA UMA ESTRUTURA DE LAÇO PARA REALIZAR UMA SOMA ACUMULATIVA ATÉ QUE ELA SEJA IGUAL A 5

contador = 0
soma = 0

while contador < 5:
    numero = float(input("Digite um número: "))
    soma += numero
    contador += 1

print("A soma total é:", soma)
