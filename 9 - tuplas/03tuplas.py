# Processamento de vendas por unidade
vendas_dia = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]

for produto, preco_unitario, quantidade in vendas_dia:
    total_venda = preco_unitario * quantidade
    print(f"Produto: {produto}, Preço Unitário: R$ {preco_unitario:.2f}, Quantidade: {quantidade}, Total da Venda: R$ {total_venda:.2f}")
    