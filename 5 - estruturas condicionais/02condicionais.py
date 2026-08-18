# Controle de acesso ao Sistema
admins = ["tokyo@empresa.com", "vitor@empresa.com", "gestor@empresa.com"]

email_antigo = input("Digite seu email: ")
dominio = "@empresa.com"

posicao_arroba = email_antigo.find("@") #encontra a posição do arroba na string
nome_usuario = email_antigo[:posicao_arroba] #pega a parte do email antes do arroba
email_dominio = nome_usuario + dominio #concatena o nome do usuário com o novo domínio
email_novo = email_dominio.lower().strip()

if email_novo in admins:
    print(f"Acesso liberado! Bem vindo administrador {nome_usuario}.")
    if email_novo != email_antigo:
        print(f"Seu email foi atualizado para {email_novo}.")

    if email_novo == "tokyo@empresa.com":
        print("Você tem acesso total ao sistema.")
    elif email_novo == "vitor@empresa.com":
        print("Você tem acesso total ao sistema. Bem vindo de volta, Vitor!")
    elif email_novo == "gestor@empresa.com":
        print("Você tem acesso restrito ao sistema.")

else:
    print(f"Acesso negado. Você não é um administrador.")