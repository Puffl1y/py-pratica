compras = []

while True:
    print("\n1 - Adicionar")
    print("2 - Mostrar")
    print("3 - Alterar")
    print("4 - Remover")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        item = input("Item: ")
        compras.append(item)

    elif opcao == "2":
        for i, item in enumerate(compras):
            print(f"{i} - {item}")

    elif opcao == "3":
        indice = int(input("Índice: "))
        novo = input("Novo nome: ")
        compras[indice] = novo

    elif opcao == "4":
        indice = int(input("Índice: "))
        compras.pop(indice)

    elif opcao == "5":
        break