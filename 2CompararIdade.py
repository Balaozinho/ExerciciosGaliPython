# Exercício 2 - PEÇA PARA O USUÁRIO INFORMAR A PRÓPRIA IDADE E A DE UM AMIGO
#UTILIZE COMPARADORES PARA RETORNAR UM BOOLEANO E VERIFICAR SE AS PERGUNTAS SÃO TRUE OR FALSE

sua_idade = int(input("Digite sua idade: "))
idade_amigo = int(input("Digite a idade do seu amigo: "))

print("As idades são iguais?", sua_idade == idade_amigo)
print("Você é mais velho que seu amigo?", sua_idade > idade_amigo)
print("Você é mais novo que seu amigo?", sua_idade < idade_amigo)
