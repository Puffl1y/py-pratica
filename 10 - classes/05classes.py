# Sistema de reservas de assento onibus

class Onibus:

    def __init__(self, destino, assentos):
        self.destino = destino
        self.assentos = assentos

    def reservar_assento(self, numero_assento):
        indice = numero_assento - 1

        if not self.assentos[indice]:
            self.assentos[indice] = True
            print(f"Assento {numero_assento} reservado com sucesso para o destino {self.destino}.")
        else:
            print(f"Assento {numero_assento} já está reservado.")

    def exibir_assentos(self):
        print(f"\nAssentos do ônibus para {self.destino}:")

        for i in range(len(self.assentos)):
            status = "Reservado" if self.assentos[i] else "Disponível"
            print(f"Assento {i + 1}: {status}")

    def quantidade_assentos_disponiveis(self):
        return self.assentos.count(False)


# Programa principal
destino = input("Digite o destino do ônibus: ")

# 10 assentos inicialmente livres
assentos = [False] * 10

onibus = Onibus(destino, assentos)

while True:

    print("\n=== MENU DE RESERVAS ===")
    print("1. Reservar assento")
    print("2. Exibir assentos")
    print("3. Quantidade de assentos disponíveis")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':

        numero_assento = int(
            input("Digite o número do assento que deseja reservar (1-10): ")
        )

        if 1 <= numero_assento <= 10:
            onibus.reservar_assento(numero_assento)
        else:
            print("Número de assento inválido.")

    elif opcao == '2':
        onibus.exibir_assentos()

    elif opcao == '3':
        quantidade = onibus.quantidade_assentos_disponiveis()
        print(f"Quantidade de assentos disponíveis: {quantidade}")

    elif opcao == '4':
        print("Saindo do sistema de reservas.")
        break

    else:
        print("Opção inválida.")