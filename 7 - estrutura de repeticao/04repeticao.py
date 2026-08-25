#analise de custos mensais
metas = {"jan": 1000, "fev": 1200, "mar": 1100} 
gastos = {"jan": 900, "fev": 1350, "mar": 1100}

for mes in metas:
    meta = metas[mes]
    gasto = gastos[mes]
    if gasto <= meta:
        print(f"{mes.capitalize()}: Dentro do orçamento. Meta: R${meta}, Gasto: R${gasto}")
    else:
        print(f"{mes.capitalize()}: Acima do orçamento! Meta: R${meta}, Gasto: R${gasto}")