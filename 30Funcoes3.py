#EXERCICIO 30 - BATALHA POKEMON

#CRIE UM PROGRAMA QUE SIMULE UMA RODADA DE BATALHA ENTRE DOIS POKEMONS ESCOLHIDOS
#O JOGADOR DEVERÁ ESCOLHER ENTRE O CHARMANDER, SQUIRTLE E BULBASSAURO
#CADA POKEMON POSSUI AS SEGUINTES CARACTERÍSTICAS
#CHARMANDER, VIDA: 100, ATAQUE: BOLA DE FOGO, DANO: 35
#SQUIRTLE, VIDA: 100, ATAQUE: JATO DE ÁGUA, DANO: 32
#BULBASSAURO, VIDA: 100, ATAQUE: CHICOTE DE PLANTA, DANO: 30

import random

pokemons = {
    'Charmander':{'Ataque': 'Bola de fogo','Dano':35},
    'Squirtle':{'Ataque': 'Jato de água','Dano': 32},
    'Bulbassauro':{'Ataque':'Chicote de planta','Dano':30},
}

jogador1 = ''
jogador2 = ''

def selecionar_pokemon(jogador) :
    print ('Escolha seu pokemon'.center(40,'-'))
    print ('(1) Charmander\n(2) Squirtle\n(3) Bulbassauro')
    print ('-'*40)
    escolha = int(input('escolha um dos pokemons: '))
    if escolha == 1:
        escolha = 'Charmander'
    elif escolha == 2:
        escolha = 'Squirtle'
    elif escolha == 3:
        escolha = 'Bulbassauro'
    else :
        print ('Não entendi! Selecione uma opção entre (1), (2) e (3)')
    
    return escolha

escolha1 = selecionar_pokemon(jogador1)
escolha2 = selecionar_pokemon(jogador2)

print (f'O jogador1 escolhe {escolha1}')
print (f'O jogador2 escolhe {escolha2}')


def ficha_habilidades(jogador) :
    print("FICHA HABILIDADES".center(40,"*"))
    print(f'Vida = 100| Ataque = {pokemons[jogador]['Ataque']}| Dano = {pokemons[jogador]['Dano']}')

print('-'*40) 
ficha_habilidades(escolha1)
ficha_habilidades(escolha2)

def ataque(escolha):
    return pokemons[escolha]['Dano']*random.uniform(1,2)

print('-'*40)
dano1 = ataque(escolha1)
dano2 = ataque(escolha2)

print(f'O dano de {jogador1} foi de {pokemons[escolha1]['Dano']*random.uniform(1,2):.2f}')
print(f'O dano de {jogador2} foi de {pokemons[escolha2]['Dano']*random.uniform(1,2):.2f}')


ataque(escolha1)
ataque(escolha2)

def batalha():
    vida1 = 100 - dano2
    vida2 = 100 - dano1
    if vida1 > vida2 :
        print(f'O vencedor foi {escolha1} pois {escolha2} ficou com menos vida: {vida2:.2f}')
    else:
        print(f'O vencedor foi {escolha2} pois {escolha1} ficou com menos vida: {vida1:.2f}')

print("-"*40)
batalha()