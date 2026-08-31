# Gestão de chamadas de suporte
def resumo_chamadas(tempos):
    quantidade_chamados = len(tempos)
    maior = max(tempos)

    return maior, quantidade_chamados


tempos = [15, 45, 10, 120, 30]
chamado_maior, quantidade = resumo_chamadas(tempos)


print(f"Foram abertos {quantidade} chamados hoje. \nTempo maximo de chamado: {chamado_maior} minutos.")