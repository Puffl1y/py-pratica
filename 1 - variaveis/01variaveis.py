# Calculo de bônus de vendas para os funcionários de uma empresa
faturamento_inicial = float(input("Digite o total de vendas: "))
percentual_bonus =  0.1

bonus_total = faturamento_inicial * percentual_bonus
print("O valor do bônus é: ", bonus_total)

faturamento_final = faturamento_inicial - bonus_total
print("O faturamento final é: ", faturamento_final)