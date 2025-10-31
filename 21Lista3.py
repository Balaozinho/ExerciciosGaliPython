#EXERCICIO 20 - CRIE UM PROGRAMA QUE GERE UM CONJUNTO DE EQUIPAMENTOS (SET) COMPLETO PARA UM PLAYER
#O SET DEVE CONTER: Set = [Boots, Pants, Armor, Helmet, Gloves, Weapon]
#SEU PROGRAMA DEVE:
#1. ESCOLHER ALEATORIAMENTE UM ITEM DE CADA LISTA (USE O RANDOM.CHOICE)
#2. MONTAR O SET COMPLETO COM ITENS SORTEADOS
#3. EXIBER CADA ITEM ESCOLHIDO E SEU PODER
#4. CALCULAR O PODER TOTAL DO SET

import random

# Listas de itens e seus valores de poder
boots_list = [['Bota Bronze', 10], ['Bota Prata', 20], ['Bota Ouro', 30]]
pants_list = [['Calça Bronze', 15], ['Calça Prata', 25], ['Calça Ouro', 35]]
armor_list = [['Armadura Bronze', 20], ['Armadura Prata', 30], ['Armadura Ouro', 40]]
helmet_list = [['Capacete Bronze', 12], ['Capacete Prata', 22], ['Capacete Ouro', 32]]
gloves_list = [['Luva Bronze', 8], ['Luva Prata', 18], ['Luva Ouro', 28]]
weapon_list = [['Espada Bronze', 25], ['Espada Prata', 35], ['Espada Ouro', 45]]

# Estrutura de referência
set_parts = ['Boots', 'Pants', 'Armor', 'Helmet', 'Gloves', 'Weapon']

# Lista com todas as listas de equipamentos
listas_itens = [boots_list, pants_list, armor_list, helmet_list, gloves_list, weapon_list]

# Lista que armazenará o set final do NPC
npc_set = []

print("🎲 Gerando set aleatório do NPC...\n")

# Percorre todas as listas de itens e escolhe 1 item aleatoriamente
for i in range(len(listas_itens)):
    item_escolhido = random.choice(listas_itens[i])
    npc_set.append(item_escolhido)
    print(f"{set_parts[i]}: {item_escolhido[0]} (Poder: {item_escolhido[1]})")

# Calcula o poder total do set
poder_total = sum(item[1] for item in npc_set)

print("\n🛡️ SET FINAL DO NPC 🛡️")
print([item[0] for item in npc_set])
print(f"\n💥 Poder Total: {poder_total}")
