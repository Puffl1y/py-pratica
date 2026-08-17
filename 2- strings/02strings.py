# Padronização de texto
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")

nome_corrigido = nome.strip().title()
email_corrigido = email.lower().strip()

print("nome:", nome_corrigido, "email:", email_corrigido)