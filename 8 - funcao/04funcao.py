# Analisador de margem de lucro

def analisar_margem(faturamento, custo):
    if faturamento <= 0 or custo < 0:
        return "Valores inválidos. O faturamento deve ser maior que zero e o custo não pode ser negativo."

    lucro = faturamento - custo
    margem_lucro = (lucro / faturamento) * 100

    if margem_lucro >= 30:
        return f"Margem de lucro Saudavel, margem = {margem_lucro:.2f}%."
    elif margem_lucro < 30 and margem_lucro > 0:
        return f"Margem de lucro baixa, margem = {margem_lucro:.2f}%."
    elif margem_lucro == 0:
        return "Sem lucro, sem prejuízo."
    else:
        return f"Margem de lucro de {margem_lucro:.2f}%."


faturamento = float(input("Digite o faturamento: "))
custo = float(input("Digite o custo: "))
resultado = analisar_margem(faturamento, custo)
print(resultado)