# Agenda de contatos
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def atualizar_telefone(self, novo_telefone):
        self.telefone = novo_telefone

    def atualizar_email(self, novo_email):
        self.email = novo_email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")

contatos = []
while True:
    print("\nMenu de Contatos:")
    print("1. Adicionar contato")
    print("2. Atualizar telefone")
    print("3. Atualizar email")
    print("4. Exibir informações do contato")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        contatos.append(Contato(nome, telefone, email))
        print(f"Contato {nome} adicionado com sucesso!")

    elif opcao == '2':
        nome = input("Digite o nome do contato para atualizar o telefone: ")
        for contato in contatos:
            if contato.nome == nome:
                novo_telefone = input("Digite o novo telefone: ")
                contato.atualizar_telefone(novo_telefone)
                print(f"Telefone do contato {nome} atualizado com sucesso!")
                break
        else:
            print(f"Contato {nome} não encontrado.")

    elif opcao == '3':
        nome = input("Digite o nome do contato para atualizar o email: ")
        for contato in contatos:
            if contato.nome == nome:
                novo_email = input("Digite o novo email: ")
                contato.atualizar_email(novo_email)
                print(f"Email do contato {nome} atualizado com sucesso!")
                break
        else:
            print(f"Contato {nome} não encontrado.")

    elif opcao == '4':
        nome = input("Digite o nome do contato para exibir informações: ")
        for contato in contatos:
            if contato.nome == nome:
                contato.exibir_informacoes()
                break
        else:
            print(f"Contato {nome} não encontrado.")

    elif opcao == '5':
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")