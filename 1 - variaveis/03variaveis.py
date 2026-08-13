# Divisão de cargas
carga_total = float(input("Digite o número de caixas a serem transportadas: "))
carga_por_caminhao = 12

# calcular quantos caminhões sairam completamente cheios
# e quantas caixas sobraram para o último caminhão

chaminhoes_cheios = carga_total // carga_por_caminhao
caixas_sobrando = carga_total % carga_por_caminhao

print("Número de caminhões completamente cheios: ", chaminhoes_cheios)
print("Número de caixas sobrando para o último caminhão: ", caixas_sobrando)