# Controle de estoque de produtos
estoque_produtos = int(input("Digite a quantidade inicial de produtos em estoque: "))

quantidade_vendida = int(input("Digite a quantidade de produtos vendidos: "))

quantidade_reposicao = int(input("Digite a quantidade de produtos repostos: "))

estoque_produtos = estoque_produtos - quantidade_vendida + quantidade_reposicao

print("O estoque atual de produtos é: ", estoque_produtos)