# Busca e extensão de listas
rota = ["Campinas", "São Paulo", "Rio de Janeiro", ]
entrada = input("Digite o nome das novas cidades: ")
rota.append(entrada)

busca = input("Digite o nome da cidade que deseja buscar: ")

posicao = rota.index(busca)

if posicao >= 0:
    print(f"A cidade {busca} está na posição {posicao} da lista.")

for i in range(len(rota)):
    print(i, rota[i])