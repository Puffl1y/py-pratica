# Calculadora de impostos
def calcular_inss(valor):
    if valor > 5000.00:
        return  valor * 0.08
    else:
        return  valor * 0.03


valor = float(input("Digite o valor do servico: "))
inss = calcular_inss(valor)

print(f"O valor do INSS a ser pago é: R$ {inss:.2f}")