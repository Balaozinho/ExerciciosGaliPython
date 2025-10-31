#EXERCICIO 24 - CONSTRUA UM MINI SISTEMA QUE ANALISA UMA LISTA DE PEDIDOS FEITO EM UMA LOJA VIRTUAL
#CADA PEDIDO É REPRESENTADO POR UMA TUPLA (PRODUTO, CATEGORIA, VALOR, STATUS)

pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]

#MOSTRE TODOS OS PRODUTOS ENTREGUES, UM POR LINHA
#CALCULE O VALOR TOTAL DOS PRODUTOS ENTREGUES
#MOSTRE OS ÚLTIMOS 3 PEDIDOS FEITOS
#CONTE QUANTOS PEDIDOS DA CATEGORIA VESTUÁRIO FORAM CANCELADOS
#PERGUNTE AO USUÁRIO UMA CATEGORIA E MOSTRE OS PEDIDOS QUE PERTENCEM À ELA

#DICAS: 
#USE INDEXAÇÃO, SLICING, LAÇOS, CONDICIONAIS E VARIÁVEIS ACUMULADORAS

valor_entregues = 0

#produtos entregues
print("PRODUTOS ENTREGUES")
for p in pedidos:
    if p[3] == "Entregue":
        print(f'- {p[0]}')
        valor_entregues += p[2]
print(f'Valor total dos entregues: R$ {valor_entregues}')

#últimos 3 pedidos
for p in pedidos[-4:]:
    if p[3] != "Cancelado":
        print(p[0])

#Cancelados da categoria Vestuário
vest_cancelado = 0
for p in pedidos:
    if p[1] == "Vestuário" and p[3] == "Cancelado":
        vest_cancelado += 1

#filtro
categoria_procura = input("Digite uma categoria para filtrar:\n-Vestuário\n-Calçados\n-Eletrônicos\nDigite aqui: ").strip().lower()
for p in pedidos:
    if p[1].lower() == categoria_procura:
        print(f'- {p[0]}')



