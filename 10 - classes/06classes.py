# Loja Virtual

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def ver_produto(self):
        print(f"Produto: {self.nome}, Preço: R${self.preco:.2f}")


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)


blusa = Produto("Blusa", 49.90)
calca = Produto("Calça", 89.90)
bota = Produto("Bota", 129.90)
camiseta = Produto("Camiseta", 29.90)
carrinho = Carrinho()

while True:
    print("\n=== MENU DA LOJA VIRTUAL ===")
    print("1. Adicionar produto ao carrinho")
    print("2. Ver produtos no carrinho")
    print("3. Calcular total do carrinho")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\nProdutos disponíveis:")
        print("1. Blusa - R$49.90")
        print("2. Calça - R$89.90")
        print("3. Bota - R$129.90")
        print("4. Camiseta - R$29.90")

        escolha = input("Digite o número do produto que deseja adicionar: ")

        if escolha == '1':
            carrinho.adicionar_produto(blusa)
            print("Blusa adicionada ao carrinho.")
        elif escolha == '2':
            carrinho.adicionar_produto(calca)
            print("Calça adicionada ao carrinho.")
        elif escolha == '3':
            carrinho.adicionar_produto(bota)
            print("Bota adicionada ao carrinho.")
        elif escolha == '4':
            carrinho.adicionar_produto(camiseta)
            print("Camiseta adicionada ao carrinho.")
        else:
            print("Opção inválida.")

    elif opcao == '2':
        if not carrinho.produtos:
            print("O carrinho está vazio.")
        else:
            print("\nProdutos no carrinho:")
            for produto in carrinho.produtos:
                produto.ver_produto()

    elif opcao == '3':
        total = carrinho.calcular_total()
        print(f"\nTotal do carrinho: R${total:.2f}")

    elif opcao == '4':
        break

    else:
        print("Opção inválida.")