# padronização email
email_antigo = input("Digite seu email: ")
dominio = "@novogrupo.com"

posicao_arroba = email_antigo.find("@") #encontra a posição do arroba na string
nome_usuario = email_antigo[:posicao_arroba] #pega a parte do email antes do arroba
email_novo = nome_usuario + dominio #concatena o nome do usuário com o novo domínio

print(f"Seu email padronizado é: {email_novo}")