# Sistema de rh - media de desempenho
desempenho ={"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}

for funcionario, notas in desempenho.items():
    media = sum(notas) / len(notas)
    print(f"{funcionario}: Média de desempenho = {media:.2f}")