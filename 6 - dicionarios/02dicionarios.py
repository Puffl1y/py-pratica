# Consulta de estoque 
estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
produto = input("Digite o nome do produto: ")
if produto in estoque:
    print(f"Temos {estoque[produto]} unidades de {produto} em estoque.")
else:
    print("Produto não encontrado em estoque.")