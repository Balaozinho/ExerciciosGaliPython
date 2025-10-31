#EXERCICIO 21 - SISTEMA DE ANÁLISE DE DESEMPENHO DE ARENAS
#VOCÊ TEM 3 PLAYERS QUE JOGARAM EM 5 ARENAS, APURANDO SUAS PONTUAÇÕES NA LISTA ARENAS
#SUA FUNÇÃO É CALCULAR A MÉDIA DE PONTOS DE CADA PLAYER
#ARMAZENAR AS MÉDIAS EM UMA NOVA LISTA
#IDENTIFICAR QUAL JOGADOR TEVE A MELHOR MÉDIA DE TODAS AS ARENAS JOGADAS
#DICAS: UTILIZE FOR, ENUMERATE, MÉTODOS DE LISTAS COMO O SUM, LEN, APPEND E INDEX
#MOSTRE TODOS OS RESULTADOS EM TELA

arenas = [
    [1200, 1500, 1100, 1800, 1700],
    [1000, 950, 1100, 1050, 980],
    [2000, 1900, 1950, 2100, 2200],
]

media_arenas = []

#CALCULAR A MÉDIA DE PONTOS DOS JOGADORES
for i, p in enumerate(arenas):
    media = sum(p)/len(p)
    print(f'A média do jogador {i+1} é de {media}')
    media_arenas.append(media)

print(media_arenas)

#IDENTIFICAR ARENA COM O MELHOR DESEMPENHO
melhor_desempenho = media_arenas.index(max(media_arenas))
print(f'A arena com o melhor desempenho é: {melhor_desempenho + 1}')
