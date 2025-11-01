
#EXERCICIO 28 - AGTECH E UMIDADE
#CRIE UMA FUNÇÃO CHAMADA VERIFICAR_UMIDADE QUE RECEBA UM VALOR D EUMIDADE E RETORNE UMA MENSAGEM
# - SE UMIDADE < 30 -> SOLO SECO, IRRIGAÇÃO NECESSÁRIA
# - SE UMIDADE ENTRE 30 E 60 -> UMIDADE IDEAL
# - SE UMIDADE < 30 -> SOLO ENCHARCADO, INTERROMPER IRRIGAÇÃO
#CRIE UMA LISTA COM AS UMIDADES DE 5 SENSORES E USE UM LAÇO PARA IMPRIMIR O RESULTADO DA FUNÇÃO DE CADA SENSOR


# Função que analisa a umidade do solo
def verificar_umidade(umidade):
    if umidade < 30:
        return "Solo seco — irrigação necessária!"
    elif umidade <= 60:
        return "Umidade ideal!"
    else:
        return "Solo encharcado — interromper irrigação!"

# Lista de leituras de sensores (em %)
umidades = [25, 45, 70, 50, 20]

# Contador de áreas que precisam de irrigação
contador_irrigar = 0

# Laço para exibir resultados
for valor in umidades:
    resultado = verificar_umidade(valor)
    print(f"Sensor: {valor}% → {resultado}")
    if "irrigação necessária" in resultado:
        contador_irrigar += 1

print(f"\nÁreas que precisam de irrigação: {contador_irrigar}")
