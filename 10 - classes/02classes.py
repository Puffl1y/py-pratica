# Sistema de biblioteca

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False


    def emprestar(self):
        if self.emprestado:
            print("Livro já emprestado.")
        else:
            self.emprestado = True
            print("Livro emprestado com sucesso!")

    def devolver(self):
        self.emprestado = False
        print("Livro devolvido.")

    def exibir_status(self):
        status = "Emprestado" if self.emprestado else "Disponível"

        print(f"\nTítulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Status: {status}")


livros = [
    Livro("Dom Casmurro", "Machado de Assis"),
    Livro("1984", "George Orwell"),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
]

print("Bem-vindo à Biblioteca!\n")
print("Livros disponíveis:")
for i, livro in enumerate(livros):
    print(f"{i + 1} - {livro.titulo}")

escolha = int(input("\nEscolha um livro para empréstimo: "))

if 1 <= escolha <= len(livros):
    livros[escolha - 1].emprestar()

print("\n--- STATUS FINAL ---")

for livro in livros:
    livro.exibir_status()