# calculo de comissão progressiva
vendas = [2000, 5000, 1000, 8000, 3000]

for i in range(len(vendas)):
    if vendas[i] <= 3000:
        comissao = vendas[i] * 0.05
    elif vendas[i] <= 7000:
        comissao = vendas[i] * 0.10
    else:
        comissao = vendas[i] * 0.15
    print(f"Vendas: R${vendas[i]:.2f} - Comissão: R${comissao:.2f}")