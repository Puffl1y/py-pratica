#Atualização de preços interativa
precos = []
produtos = []

while True:
    preco = float(input("Digite o preço do produto (ou 0 para sair): "))
    produto = input("Digite o nome do produto: ")
    if preco == 0:
        break
    precos.append(preco)
    produtos.append(produto)

print("Preços atualizados:", precos)
print("Produtos:", produtos)