# analise de dados de vendas
Vendas = [1500, 2000, 800, 3500, 1200]

total_vendas = sum(Vendas)
quantidade_vendas = len(Vendas)
media_vendas = total_vendas / quantidade_vendas

maior_venda = max(Vendas)
menor_venda = min(Vendas)
print(f"Total: {total_vendas}, Média: {media_vendas:.2f}, Quantidade de vendas: {quantidade_vendas}, Maior venda: {maior_venda}, Menor venda: {menor_venda}")