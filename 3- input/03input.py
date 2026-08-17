# Coletando dados de faturamento de lojas
loja_a = float(input("Digite o faturamento da loja A: "))
loja_b = float(input("Digite o faturamento da loja B: "))

total = loja_a + loja_b
media = total / 2

print(f"Total: {total:.2f} media: {media:.2f}")

if (loja_a > loja_b):
    print(f"A loja A faturou mais, com um total de: R$ {loja_a:.2f}")

elif (loja_b > loja_a):
    print(f"A loja B faturou mais, com um total de: R$ {loja_b:.2f}")

elif (loja_b == loja_a):
    print("Os faturamentos das duas lojas são iguais")