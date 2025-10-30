# Exercício 9 - FAÇA UMA TABUADA PERSONALIZADA
#SEU SISTEMA DEVE PEDIR UM NÚMERO PARA O USUÁRIO E LOGO EM SEGUIDA A TABUADA DAQUELE NÚMERO DEVE SER CALCULADA
#CADA RESULTADO PRECISA SER DEMONSTRADO

numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
