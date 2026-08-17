
nome = input("Digite seu nome: ")

find_nome = nome.find(" ") #encontra a posição do espaço na string
primeiro_nome = nome[:find_nome] #pega a parte do nome antes do espaço
primeiro_nome_maiusculo = primeiro_nome.title()
print(f"Olá, {primeiro_nome_maiusculo}! Seja bem-vindo(a)!")