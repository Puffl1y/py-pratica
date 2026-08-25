# reajuste geral de preços
precos = {"celular": 1500, "tablet": 2500, "notebook": 5000}
aumento = 0.10

for produto, preco in precos.items():
    novo_preco = preco * (1 + aumento)
    print(f"{produto.capitalize()}: Preço antigo: R${preco:.2f}, Novo preço: R${novo_preco:.2f}")