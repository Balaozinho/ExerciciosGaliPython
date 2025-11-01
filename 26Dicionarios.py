# Exercício 26 - Evolução do personagem
#Crie um dicionário chamado player que armazene as informações de um personagem de RPG
# nome, classe, nível e atributos (outro dict com força, agilidade e inteligência)
#Aumente o nível do player em 1 e utilize um fator de 1.1 para multiplicar a força, agilidade e inteligência atual

player = {
    "nome": "Arwen",
    "classe": "Maga",
    "nivel": 10,
    "atributos": {
        "forca": 15,
        "agilidade": 22,
        "inteligencia": 40
    }
}

print("🎮 Status inicial:")
for chave, valor in player["atributos"].items():
    print(f"{chave.capitalize()}: {valor}")

# Evolução de nível
player["nivel"] += 1
for atributo in player["atributos"]:
    player["atributos"][atributo] *= 1.1  # aumento de 10%

print(f"\n✨ {player['nome']} subiu para o nível {player['nivel']}!")

print("\n🔮 Novos atributos:")
for chave, valor in player["atributos"].items():
    print(f"{chave.capitalize()}: {valor:.1f}")
