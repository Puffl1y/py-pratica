# Sistema de triagem de emails

assunto = input("Digite o assunto do email: ").lower().strip()
texto = input("Digite o texto do email: ").lower().strip()

if "pagamento" in assunto or "boleto" in assunto or "fatura" in assunto:
    print("Email encaminhado para o financeiro.")
elif "entrega" in assunto or "rastreamento" in assunto or "pedido" in assunto:
    print("Email encaminhado para o setor de logística.")
elif "reclamação" in assunto or "problema" in assunto or "erro" in assunto:
    print("Email encaminhado para o setor de atendimento ao cliente.")
else:
    print("Email encaminhado para o suporte geral.")