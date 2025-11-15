#EXERCICIO 38
#CRIE UM PROGRAMA QUE: 
#1. O USUÁRIO INFORME DOIS NÚMEROS 
#2. REALIZE A DIVISÃO ENTRE O 1° NUMERO E O 2° NUMERO
#3. TRATE OS CENÁRIOS EM QUE: USUÁRIO DIGITA ALGO DIF DE UM NÚMERO OU, 
#SE TENTAR DIVIDIR POR ZERO
#UTILIZE ELSE
#UTILIZE FINALLY PARA EXIBIR MENSAGEM DE ENCERRAMENTO, COMO: 
#"PROGRAMA FINALIZADO. OBRIGADO POR USAR A CALCULADORA"


try:
    # Solicita os números do usuário
    numerador = float(input("Digite o numerador: "))
    denominador = float(input("Digite o denominador: "))

    # Tenta realizar a divisão
    resultado = numerador / denominador

# Trata erro de divisão por zero
except ZeroDivisionError:
    print("❌ Erro: Não é possível dividir por zero!")

# Trata erro de valor inválido (quando não é número)
except ValueError:
    print("❌ Erro: Digite apenas números válidos!")

# Executa se nenhum erro ocorrer
else:
    print(f"✅ Resultado da divisão: {resultado}")

# Executa sempre, com ou sem erro
finally:
    print("🔚 Programa finalizado. Obrigado por usar a calculadora!")
