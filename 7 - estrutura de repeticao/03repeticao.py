# verificação estoque
estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
estoque_quantidades = [5, 12, 2, 8, 15]

for i in range(len(estoque_produtos)):
    produto = estoque_produtos[i]
    quantidade = estoque_quantidades[i]
    
    if quantidade < 8:
        print(f"ALERTA: Produto: {produto} - Estoque baixo! Quantidade: {quantidade}")
    else:
        print(f"Produto: {produto} - Estoque suficiente. Quantidade: {quantidade}")