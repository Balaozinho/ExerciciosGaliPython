# 🌾 Exercício 25 - Sistema de Gestão da Fazenda

#CRIE UM PEQUENO SISTEMA DE CONTROLE DE LAVOURAS, ONDE CADA LAVOURA POSSUI INFORMAÇÕES COMO:
# CULTURA PLANTADA, ÁREA EM HECTARES, PRODUTIVIDADE MÉDIA (SACAS/HA), PREÇO DA SACA (R$)
#O PROGRAMA DEVE MOSTRAR UM RELATÓRIO COMPLETO DE TODAS AS LAVOURAS
#CALCULE A PRODUÇÃO TOTAL EM SACAS E O FATURAMENTO TOTAL ESTIMADO
#MOSTRE QUAL CULTURA TEM O MAIOR FATURAMENTO INDIVIDUAL

fazenda = {
    "Soja": {
        "area_ha": 120,
        "produtividade": 55,
        "preco_saca": 145.00
    },
    "Milho": {
        "area_ha": 80,
        "produtividade": 70,
        "preco_saca": 65.00
    },
    "Café": {
        "area_ha": 40,
        "produtividade": 30,
        "preco_saca": 920.00
    }
}

print("🌽 RELATÓRIO DE PRODUÇÃO AGRÍCOLA 🌾")
print("-" * 45)

faturamento_total = 0
maior_faturamento = 0
melhor_cultura = ""

for cultura, dados in fazenda.items():
    producao = dados["area_ha"] * dados["produtividade"]
    faturamento = producao * dados["preco_saca"]
    faturamento_total += faturamento

    print(f"Cultura: {cultura}")
    print(f"  Área plantada: {dados['area_ha']} ha")
    print(f"  Produtividade média: {dados['produtividade']} sc/ha")
    print(f"  Produção total: {producao} sacas")
    print(f"  Faturamento estimado: R$ {faturamento:,.2f}\n")

    # Verifica cultura mais rentável
    if faturamento > maior_faturamento:
        maior_faturamento = faturamento
        melhor_cultura = cultura

print("-" * 45)
print(f"💰 Faturamento total estimado: R$ {faturamento_total:,.2f}")
print(f"🏆 Cultura mais lucrativa: {melhor_cultura} (R$ {maior_faturamento:,.2f})")
