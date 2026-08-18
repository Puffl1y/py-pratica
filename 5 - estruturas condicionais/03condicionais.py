# Desconto progressivo
valor_compra = float(input("Digite o valor da compra: "))
numero_itens = int(input("Digite o número de itens comprados: "))

if valor_compra >= 500:
    desconto = 0.15
elif valor_compra >= 200 and valor_compra < 500:
    desconto = 0.1
else:
    desconto = 0

if numero_itens > 4:
    desconto += 0.1
elif numero_itens > 2 and numero_itens <= 4:
    desconto += 0.05
    
valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")