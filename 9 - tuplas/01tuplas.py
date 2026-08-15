# coordenadas
coordenadas = input("Digite as coordenadas separadas por vírgula (x,y): ")

x, y = coordenadas.split(",") #divide a srtring em duas partes, separadas pela vírgula

print(f"Coordenada X: {x.strip()}") #.strip() remove espaços em branco no início e no final da string
print(f"Coordenada Y: {y.strip()}")