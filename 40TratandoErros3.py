#CRIE UMA FUNÇÃO CADASTRAR_USUARIO(NOME, IDADE) QUE:
#1. LANCE UMA EXCEÇÃO PERSONALIZADA IdadeInvalidaError SE A IDADE < 13
#2. LANCE UM ValueError SE O NOME ESTIVER VAZIO
#3. CASO ESTEJA TUDO CERTO, EXIBA "USUÁRIO CADASTRADO COM SUCESSO!"

#DEPOIS: 
#PEÇA PARA O USUÁRIO O NOME E A IDADE
#CHAME A FUNÇÃO DENTRO DE UM BLOCO TRY/EXCEPT
#TRATE SEPARADAMENTE OS DOIS TIPOS DE ERRO (IdadeInvalidaError E ValueError)
#USE ELSE PARA CONFIRMAR O SUCESSO
#E FINALLY PARA EXIBIR "PROCESSO DE CADASTRO ENCERRADO"


# Criando exceção personalizada
class IdadeInvalidaError(Exception):
    pass

# Função principal
def cadastrar_usuario(nome, idade):
    if not nome.strip():
        raise ValueError("O nome não pode estar vazio.")
    if idade < 13:
        raise IdadeInvalidaError("Usuário deve ter pelo menos 13 anos para se cadastrar.")
    print(f"✅ Usuário '{nome}' cadastrado com sucesso!")

# Programa principal
try:
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))

    cadastrar_usuario(nome, idade)

except ValueError as erro:
    print("❌ Erro de valor:", erro)

except IdadeInvalidaError as erro:
    print("❌ Erro de idade:", erro)

else:
    print("🎉 Cadastro concluído sem erros!")

finally:
    print("🔚 Processo de cadastro encerrado.")
