# conversão de tempo
duracao_contrato = int(input("Digite a duração do contrato em meses: "))
duracao_contrato_anos = int(duracao_contrato / 12)
meses_restantes = duracao_contrato % 12
print("A duração do contrato é: ", duracao_contrato_anos, "anos e ", meses_restantes, "meses.")