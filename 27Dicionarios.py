#EXERCICIO 27 - CRIE UM SISTEMA DE GERENCIAMENTO DE PRODUTOS EM UMA LOJA DE GAMES. SEU OBJETIVO É:
#CADASTRAR EM UM DICIONÁRIO 3 JOGOS COM NOME, PREÇO E ESTOQUE
#1. EXIBIR OS JOGOS DISPONÍVEIS E SUAS INFORMAÇÕES
#2. PERMITIR QUE O USUÁRIO COMPRE JOGOS
#3. ATUALIZAR O ESTOQUE
#4. MOSTRAR RESULTADO FINAL DA COMPRA

loja_games = {
    "Minecraft" : {"Preço" : 59.90, "Estoque" : 5},
    "Fifa" : {"Preço" : 199.90, "Estoque" : 3},
    "God of war" : {"Preço" : 149.90, "Estoque" : 4},
}

carrinho = {}

print("JOGOS DISPONÍVEIS".center(50, '-'))
for j, infos in loja_games.items():
    print(f'{j} - R$ {infos['Preço']} - Estoque: {infos['Estoque']} unidades')

while True:
    escolha_usuario = input("Digite o nome do jogo que deseja ('sair' para finalizar): ").capitalize()
    if escolha_usuario == 'Sair':
        break
    if escolha_usuario in loja_games:
        qtdade = int(input("Legal! Quantas unidades você deseja? "))
        if qtdade <= loja_games[escolha_usuario]['Estoque']:
            loja_games[escolha_usuario]['Estoque'] -= qtdade
            if escolha_usuario in carrinho:
                carrinho[escolha_usuario] += qtdade
            else:
                carrinho.setdefault(escolha_usuario, qtdade)
            print(f"{qtdade} unidades do jogo {escolha_usuario} adicionado com sucesso!")
        else:
            print("Não há estoque suficiente")
    else:
        print("Jogo não encontrado, tente novamente!")

print('RESUMO DA COMPRA'.center(50, '-'))
total = 0
for jogo, qtd in carrinho.items():
    preco = loja_games[jogo]['Preço']
    total += preco * qtd
    print(f'-{jogo} x {qtd} quantidades')
 
print('-'*50)
print(f'Total R$: {total}')


