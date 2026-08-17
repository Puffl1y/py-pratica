# sistema de cadastro - padronizando nome e email
nome = input("Digite seu nome completo: ")
email = input("Digite seu email: ")

find_nome = nome.find(" ") #encontra a posição do espaço na string
primeiro_nome = nome[:find_nome] #pega a parte do nome antes do espaço
primeiro_nome_maiusculo = primeiro_nome.title()

email = email.lower().strip() #padroniza o email para minúsculo e remove espaços em branco

posicao_arroba = email.find("@") #encontra a posição do arroba na string
email_padrao = email[:posicao_arroba] + "@novogrupo.com" #concatena o nome do usuário com o novo domínio

print(f"Cadastro concluido: {primeiro_nome_maiusculo}. E-mail de acesso: {email_padrao}")