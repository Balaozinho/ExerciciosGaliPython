#EXERCÍCIO 39 
#CRIE UM PROGRAMA QUE PEÇA PARA O USUÁRIO O NOME DE UM ARQUIVO CSV PARA ABRIR
#TENTE ABRIR O ARQUIVO E MOSTRAR AS 3 PRIMEIRAS LINHAS
#SE O ARQUIVO NÃO EXISTIR, MOSTRE A MSG "ARQ NÃO ENCONTRADO"
#SE O ARQUIVO ABRIR COM SUCESSO, EXIBA "ARQUIVO LIDO COM SUCESSO"
#INDEPENDENTE DO RESULTADO, MOSTRE NO FINAL "ENCERRANDO LEITURA" E FECHE O ARQUIVO

try:
    nome_arquivo = input("Digite o nome do arquivo: ")
    arquivo = open(nome_arquivo, "r")  # tenta abrir o arquivo
    linhas = arquivo.readlines()       # lê todas as linhas
except FileNotFoundError:
    print("❌ Erro: Arquivo não encontrado!")
else:
    print("✅ Arquivo lido com sucesso! As 3 primeiras linhas são:\n")
    for linha in linhas[:3]:
        print(linha.strip())
finally:
    print("🔚 Encerrando leitura...")
    if 'arquivo' in locals():
        arquivo.close()  # fecha o arquivo se ele foi aberto
