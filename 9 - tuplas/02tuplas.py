# Resumo da folha de pagamento

def calcular_folha(salario_bruto):
    descontos = salario_bruto * 0.1 
    salario_liquido = salario_bruto - descontos 
    return salario_liquido, descontos


salario_bruto = float(input("Digite o salário bruto: "))
salario_liquido, descontos = calcular_folha(salario_bruto)
print(f"Salário líquido: R$ {salario_liquido:.2f}")
print(f"Descontos: R$ {descontos:.2f}")