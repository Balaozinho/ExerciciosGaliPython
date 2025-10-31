# Exercício 22 - Estatísticas básicas do personagem
#IMPRIMA SEPARADAMENTE O NOME, NÍVEL E CLASSE DE CADA CAVALEIRO DO ZODÍACO - UTILIZE OS CONCEITOS DE INDEXAÇÃO


cavaleiro_stats = [("Iki", 20, "Fênix"),
                 ("Shyriu", 12, "Dragão"),
                 ("Seya", 15, "Pégaso")]

for c in cavaleiro_stats:
    print("CARACTERÍSTICAS CAVALEIRO".center(40))
    print('_'*40)
    print(f"Nome:{c[0]}\nLevel:{c[1]}\nClasse: {c[2]}")
    print('-'*40)



