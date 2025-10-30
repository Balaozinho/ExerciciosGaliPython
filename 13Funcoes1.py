# Exercício 13 
#CRIE UMA FUNÇÃO CHAMADA SAUDAR E QUE RECEBA COMO PARÂMETRO O NOME DA PESSOA
#A FUNÇÃO DEVERÁ APARECER UM OLÁ COM O NOME DA PESSOA E QUE ELA SEJA MUITO BEM VINDA
#UTILIZE A FUNCAO COM UM NOME INFORMADO PELO USUÁRIO

def saudar(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a) à Galileu!")

usuario = input("Digite seu nome: ")
saudar(usuario)
