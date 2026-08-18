# Organização de preços
entrada = input("Digite números separados por vírgula: ")

numeros = entrada.split(",")
numeros = list(map(int, entrada.split(",")))

numeros.sort()

top_fretes = list(numeros[-2:])

print(f"valores dos fretes: {numeros}")
print(f"Os top fretes são: {top_fretes}")