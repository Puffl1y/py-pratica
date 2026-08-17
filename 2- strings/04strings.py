# Extração de UserName
email = input("Digite seu email: ")

find_arroba = email.find("@") #encontra a posição do arroba na string
username = email[:find_arroba] #pega a parte do email antes do arroba
print(f"Seu username é: {username}") 