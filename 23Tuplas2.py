#EXERCICIO23 - VOCÊ É RESPONSÁVEÇ PELO CONTROLE DE UM ESTOQUE DE LOJA DE INFORMÁTICA
#CADA PRODUTO É REPRESENTADO POR UMA TUPLA COM A SEGUINTE CONFIGURAÇÃO 
#(NOME, QUANTIDADE_EM_ESTOQUE)
#MOSTRE TOS PRODUTOS COM MENOS DE 5 UNIDADES EM ESTOQUE
#MOSTRE A QUANTIDADE DE PRODUTOS ZERADOS E QUAL A QUANTIDADE TOTAL DE ITENS NO ESTOQUE

estoque = (
    ('Mouse LG Tech', 10),
    ('Mic Hyper X', 5),
    ('Acer Nitro 5', 3),
    ('Webcam HD', 0)
)

soma_total = 0
soma_zerados = 0

print('PRODUTOS COM MENOS DE 5 UNIDADES:')
for p in estoque:
    soma_total += p[1]
    if p[1] < 5:
        print(f'- {p[0]}')

for p in estoque:
    if p[1] == 0:
        soma_zerados += 1

print(f'Produtos Esgotados: {soma_zerados}')
print(f'Total geral de itens no estoque: {soma_total}')
    
    