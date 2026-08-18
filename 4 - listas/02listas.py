# Gestão de estoque de produtos
produtos = []

while True:
    print("\n1 - Adicionar")
    print("2 - Mostrar")
    print("3 - Alterar")
    print("4 - Remover")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        produto = input("Produto: ")
        produtos.append(produto)

    elif opcao == "2":
        for i, produto in enumerate(produtos):
            print(f"{i} - {produto}")

    elif opcao == "3":
        indice = int(input("Índice: "))
        novo = input("Novo nome: ")
        produtos[indice] = novo

    elif opcao == "4":
        indice = int(input("Índice: "))
        produtos.pop(indice)

    elif opcao == "5":
        break