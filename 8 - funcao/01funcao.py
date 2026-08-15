# padronizar texto

produtos_baguncados = [
    "  arroz  ",
    "feijão",
    " macarrão",
    "  leite",
    "açúcar  ",
    " café",
    "pão  ",
    " manteiga",
]

def padronizar_texto(texto):
    return texto.strip().title()

produtos_padronizados = [padronizar_texto(produto) for produto in produtos_baguncados]
print(produtos_padronizados)