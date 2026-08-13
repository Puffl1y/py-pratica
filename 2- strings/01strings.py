# Margem de lucro
faturamento = int(input("Digite o faturamento: "))
custo = int(input("Digite o custo: "))
lucro = faturamento - custo
margem_lucro = (lucro / faturamento)

print("O lucro é: ", f"{lucro:.2f}")
print("A margem de lucro é: ", f"{margem_lucro:.0%}")