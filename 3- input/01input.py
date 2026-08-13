# calculadora de imposto sobre vendas

faturamento = input("Digite o valor bruto da venda: ") #valor com R$ 

faturamento = faturamento.replace("R$", "").replace(".", "").replace(",", ".")
faturamento_numerico = float(faturamento)

imposto = input("Digite o valor do imposto : ")
imposto = imposto.replace("%", "").replace(",", ".")

imposto_numerico = float(imposto)
imposto_numerico = imposto_numerico / 100

total = faturamento_numerico * imposto_numerico

print("O valor do imposto sobre vendas é: ", f"{total:.2f}")