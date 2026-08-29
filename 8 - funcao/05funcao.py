# Conversor de moeda
def converter_para_real(valor_em_dolar, taxa_cambio):
    if valor_em_dolar < 0 or taxa_cambio <= 0:
        return "Valores inválidos. O valor em dólar deve ser maior ou igual a zero e a taxa de câmbio deve ser maior que zero."

    valor_em_real = valor_em_dolar * taxa_cambio
    return f"O valor em reais é: R$ {valor_em_real:.2f}"

def processar_lista_precos(lista_precos, taxa_cambio):
    resultados = []
    for preco in lista_precos:
        resultado = converter_para_real(preco, taxa_cambio)
        resultados.append(resultado)
    return resultados

# Exemplo de uso
lista_precos_dolar = print("Digite os preços em dólar separados por vírgula (ex: 10.5, 20, 30): ")
lista_precos_dolar = input().split(',')
lista_precos_dolar = [float(preco.strip()) for preco in lista_precos_dolar]
taxa_cambio = float(input("Digite a taxa de câmbio (ex: 5.25): "))
resultados = processar_lista_precos(lista_precos_dolar, taxa_cambio)
for resultado in resultados:
    print(resultado)