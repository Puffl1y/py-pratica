# Meta de vendas de uma equipe
equipe_vendas = { "João": 12000, "Maria": 9500, "Ricardo": 10000, "Fernanda": 15200, "Paulo": 5000 }
meta_objetivo = 10000

def quem_bateu_meta(equipe, meta):
    for nome, valor in equipe.items():
        if valor >= meta:
            print(f"{nome} bateu a meta com um lucro de R$ {valor:.2f}")
        else:
            print(f"{nome} não bateu a meta.")

quem_bateu_meta(equipe_vendas, meta_objetivo)