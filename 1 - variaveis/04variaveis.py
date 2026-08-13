# Analise de margem de lucro
faturamento = float(input("Digite o faturamento total: "))
custos_fixos = float(input("Digite os custos fixos: "))
impostos = 0.15

impostos_calculados = faturamento * impostos
liquido = faturamento - custos_fixos - impostos_calculados
margem = liquido / faturamento

meta_atingida = margem > 0.3

print("O total de impostos é: ", impostos_calculados)
print("O lucro líquido é: ", liquido)
print("A margem de lucro é: ", margem)
if meta_atingida:
    print("A meta de margem de lucro foi atingida.")
