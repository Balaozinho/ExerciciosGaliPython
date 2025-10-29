# Exercício 6 - FAÇA UM SISTEMA DE LOGIN ONDE O USUÁRIO INFORME NOME E SENHA
#CONSIDERE O USUÁRIO COMO 'ADMIN' E SENHA '1234'
#CASO O USUÁRIO INFORME O LOGIN E SENHA CORRETAMENTE, RETORNE 'LOGIN BEM SUCEDIDO'
#CASO CONTRÁRIO, RETORNE 'USUÁRIO OU SENHA INCORRETO'

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")
