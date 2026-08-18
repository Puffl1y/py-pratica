# Analise de metas

vendas_vendedor = float(input("Digite o valor das vendas do vendedor: "))
vendas_loja = float(input("Digite o valor das vendas da loja: "))

meta_vendedor = 10000
meta_loja = 50000

bonus_vendedor = vendas_vendedor * 0.2


if vendas_vendedor >= meta_vendedor and vendas_loja >= meta_loja:
    print("O vendedor e a loja atingiram suas metas!")
    print(f"Seu bonus esse mes foi de: R$ {bonus_vendedor:.2f}")
else:
    print("O vendedor ou a loja não atingiram suas metas.")
    print(f"Mas não desista! faltou apenas R$ {meta_vendedor - vendas_vendedor:.2f} para o vendedor e R$ {meta_loja - vendas_loja:.2f} para a loja.")

