# Analise de faturamentos 
vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

total_vendas = sum(vendas_regiao.values())
media_vendas = total_vendas / len(vendas_regiao)

print(f"Total de vendas: R${total_vendas:.2f}")
print(f"Média de vendas por região: R${media_vendas:.2f}")