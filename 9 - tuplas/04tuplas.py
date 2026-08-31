# Perfomace de vendas regionais
def analisar_vendas(vendas):
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return total_vendas, media_vendas

dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

for filial in dados_filiais:
    vendas_filial = dados_filiais[filial]
    total_vendas_filial, media_vendas_filial = analisar_vendas(vendas_filial)
    print(f"Filial {filial} -> Total: R${total_vendas_filial}, Media: R${media_vendas_filial}")
