# Exercício 2 - Calculadora simples
#CRIE UMA FUNÇÃO DE CALCULADORA SIMPLES, QUE RECEBA COMO PARAMETRO O 1° NUMERO, 2° NÚMERO, E O CARACTER DA OPERAÇÃO DESEJADA
#FORA DA FUNÇÃO, PEÇA PARA QUE O USUÁRIO INFORME N1 E N2, ASSIM COMO A OPERAÇÃO QUE DESEJA - SEPARADAMENTE
#CRIE UMA VARIÁVEL CHAMADA RESULTADO E UTILIZE A FUNÇÃO CALCULADORA PASSANDO OS PARAMÊTROS INFORMADOS PREVIAMENTE

def calcular(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b
    else:
        return "Operação inválida!"

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

resultado = calcular(n1, n2, op)
print("Resultado:", resultado)
