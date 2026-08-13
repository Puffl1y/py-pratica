# validação de investimento
investimento = input("Digite o valor do investimento: ")
investimento = investimento.replace("R$", "").replace(",", ".").replace(".", "")
investimento = float(investimento)

if investimento < 1000:
    print("Perfil iniciante, recomendamos investir em tesouro direto")

elif investimento >= 1000 and investimento <= 50000:
    print("Perfil moderado: Sugerimos Fundos Imobiliários")

elif investimento > 50000:
    print("Perfil avançado: Sugerimos ações")

else:
    print("Erro")