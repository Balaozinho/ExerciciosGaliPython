# Exercício 5 - FAÇA O SISTEMA DE UMA LOJA CONFORME O VALOR DE VENDA DO CLIENTE
# SE ABAIXO DE 100 REAIS -> SEM DESCONTOS
# SE ENTRE 100-200 REAIS -> 5% DESCONTO
# SE ACIMA DE 200 REAIS -> 10% DESCONTO
#POR FIM, MOSTRE O PREÇO FINAL COM O DESCONTO APLICADO

valor = float(input("Digite o valor da compra: "))

if valor < 100:
    desconto = 0
elif valor <= 200:
    desconto = 0.05
else:
    desconto = 0.10

valor_final = valor - (valor * desconto)

print("Desconto aplicado:", desconto * 100, "%")
print("Valor final da compra: R$", valor_final)
