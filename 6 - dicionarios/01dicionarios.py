# Atualizando o valor de compras de clientes em um dicionário
clientes = {"Vitor": 25, "Maria": 30, "João": 20}

nova_compra = int(input("Digite o valor da nova compra: "))

cliente = input("Digite o nome do cliente: ")

if cliente in clientes:
    clientes[cliente] += nova_compra
else:
    clientes[cliente] = nova_compra

print(clientes)