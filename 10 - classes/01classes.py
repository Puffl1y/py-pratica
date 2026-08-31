# Cadastro de produtos
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_dados(self):
        print(f"\nProduto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")

    def calcular_valor_estoque(self):
        return self.preco * self.quantidade


produtos = []

for i in range(3):
    print(f"\nCadastro do produto {i + 1}")

    nome = input("Nome: ")
    preco = float(input("Preço (ex.: 2.00): "))
    quantidade = int(input("Quantidade: "))

    produto = Produto(nome, preco, quantidade)
    produtos.append(produto)

print("\n--- PRODUTOS CADASTRADOS ---")

for produto in produtos:
    produto.exibir_dados()
    print(f"Valor em estoque: R$ {produto.calcular_valor_estoque():.2f}")