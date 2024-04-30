""" programa para calcular a conta de energia elétrica de um
consumidor residencial da Equatorial MA
"""


def obter_nome_cliente():
    """ função para obter o nome do cliente"""
    print("\n\n\nBem vindo ao sistema de cálculo de conta de energia da Equatorial MA\n\n")
    return input("Entre com o nome do consumidor:  ")


def obter_tipo_tarifa():  # tipo de tarifa de energia Residencial de Equatorial MA
    """funcão para obter o tipo de tarifa de energia Residencial de Equatorial MA"""
    print("""MENU:
    [TBR] - Tarifa Baixa Renda
    [TRNC] - Tarifa Residencial Normal Convencional
    [TRNB] - Tarifa Residencial Normal Branca\n\n""")
    while True:
        tipo_tarifa = input(
            "Entre com um das opções \"TBR\",\"TRNC\" ou \"TRNB\" :")
        tipo_tarifa = tipo_tarifa.upper()
        if tipo_tarifa in ["TBR", "TRNC", "TRNB"]:
            return tipo_tarifa
        else:
            print("Opção de tarifa inválida")
            continue


def obter_consumo_total():  # consumo total de energia em kWh
    """funcão para obter o consumo total de energia em kWh"""
    return float(input("Entre com o valor de kWh consumido no mês: "))


def calcular_consumo(consumo_total, tipo_tarifa, forma_pagamento):
#calcular o valor da conta de energia para cada tipo de tarifa
#de energia Residencial de Equatorial MA
    """função para calcular o valor da conta de energia para cada tipo de tarifa de energia
Residencial de Equatorial MA"""
    # Definição de variáveis e Constantes

    # Tarifa Residencial Baixa Renda
    valor_consumo_30k = 0.23033  # Tarifa (R$/kWh)
    valor_consumo_31_100k = 0.39485  # Tarifa (R$/kWh)
    valor_consumo_101_220k = 0.59227  # Tarifa (R$/kWh)
    valor_consumo_acima_220k = 0.65808  # Tarifa (R$/kWh)
    # Tarifa Residencial Normal Convencional
    valor_consumo_convencional = 0.71881  # Tarifa (R$/kWh)
    # Tarifa Residencial Normal Branca
    valor_consumo_ponta = 1.5968  # Tarifa (R$/kWh)
    valor_consumo_intermediario = 1.01266  # Tarifa (R$/kWh)
    valor_consumo_fora_ponta = 0.57891  # Tarifa (R$/kWh)

    # inicialização de variáveis
    valor_consumo_30k = 0.0
    valor_consumo_31_100k = 0.0
    valor_consumo_101_220k = 0.0
    valor_consumo_acima_220k = 0.0

    consumo_30k = 0
    consumo_31_100k = 0
    consumo_101_220k = 0
    consumo_acima_220k = 0
    if tipo_tarifa == "TBR":
        if consumo_total <= 30:
            consumo_30k = consumo_total
        elif consumo_total > 30 and consumo_total <= 100:
            consumo_30k = 30
            consumo_31_100k = consumo_total - 30
        elif consumo_total > 100 and consumo_total <= 220:
            consumo_30k = 30
            consumo_31_100k = 70
            consumo_101_220k = consumo_total - 100
        else:
            consumo_30k = 30
            consumo_31_100k = 70
            consumo_101_220k = 120
            consumo_acima_220k = consumo_total - 220

        # Calculo do consumo Baixa Renda C
        valor_consumo_30k = consumo_30k * valor_consumo_30k
        valor_consumo_31_100k = consumo_31_100k * valor_consumo_31_100k
        valor_consumo_101_220k = consumo_101_220k * valor_consumo_101_220k
        valor_consumo_acima_220k = consumo_acima_220k * valor_consumo_acima_220k
        if forma_pagamento == "P":
            valor_conta = valor_consumo_30k + valor_consumo_31_100k + \
                valor_consumo_101_220k + valor_consumo_acima_220k
        elif forma_pagamento == "D":
            valor_conta = (valor_consumo_30k + valor_consumo_31_100k +
                           valor_consumo_101_220k + valor_consumo_acima_220k) * 1.02
        elif forma_pagamento == "C":
            valor_conta = (valor_consumo_30k + valor_consumo_31_100k +
                           valor_consumo_101_220k + valor_consumo_acima_220k) * 1.05
    elif tipo_tarifa == "TRNC":
        # Calculo do consumo Normal
        consumo_convencional = consumo_total
        valor_consumo = consumo_convencional * valor_consumo_convencional
        if forma_pagamento == "P":
            valor_conta = valor_consumo
        elif forma_pagamento == "D":
            valor_conta = valor_consumo * 1.02
        elif forma_pagamento == "C":
            valor_conta = valor_consumo * 1.05
    elif tipo_tarifa == "TRNB":
        consumo_ponta = consumo_total * .25  # 15% do consumo total
        consumo_intermediário = consumo_total * .35  # 25% do consumo total
        consumo_fora_ponta = consumo_total * .40  # 60% do consumo total
        # Calculo consumo Normal
        valor_consumo_ponta = consumo_ponta * valor_consumo_ponta
        valor_consumo_intermediario = consumo_intermediário * valor_consumo_intermediario
        valor_consumo_fora_ponta = consumo_fora_ponta * valor_consumo_fora_ponta
        if forma_pagamento == "P":
            valor_conta = valor_consumo_ponta + \
                valor_consumo_intermediario + valor_consumo_fora_ponta
        elif forma_pagamento == "D":
            valor_conta = (
                valor_consumo_ponta + valor_consumo_intermediario + valor_consumo_fora_ponta) * 1.02
        elif forma_pagamento == "C":
            valor_conta = (
                valor_consumo_ponta + valor_consumo_intermediario + valor_consumo_fora_ponta) * 1.05
    return valor_conta


def escolha_forma_pagamento():  # Escolha da forma de pagamento da conta de energia
    """função para escolha da forma de pagamento da conta de energia"""
    print("""Escolha a forma de Pagamento

    MENU:

    [P] - Pagamento com PIX sem juros

    [D] - Pagamento com Cartão de Débito com juros de 2%

    [C] - Pagamento com Cartão de Crédito com juros de 5%\n\n""")
    while True:
        forma_pagamento = input("Entre com \"P\" , \"D\" ou \"C\" : ")
        forma_pagamento = forma_pagamento.upper()
        if forma_pagamento in ["P", "D", "C"]:
            return forma_pagamento
        print("Opção inválida")


def impressao_conta(tipo_tarifa, nome_cliente, forma_pagamento, valor_conta):
    """funcão para impressão da conta de energia do consumidor"""
    if forma_pagamento == "P":
        forma_pagamento = "PIX"
    elif forma_pagamento == "D":
        forma_pagamento = "DÉBITO"
    else:
        forma_pagamento = "CRÉDITO"
    if tipo_tarifa == "TBR":
        tipo_tarifa = "Tarifa Residencial Baixa Renda Convencional"
        print("\n\n")
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {tipo_tarifa} ")
        print(
            f"O valor da conta é : R$ {valor_conta:.2f} com pagamento no {forma_pagamento}   ")
    elif tipo_tarifa == "TRNC":
        tipo_tarifa = "Tarifa Residencial Normal Convencional"
        print("\n\n")
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {tipo_tarifa} ")
        print(
            f"O valor da conta é : R$ {valor_conta:.2f} com pagamento no {forma_pagamento}   ")
    elif tipo_tarifa == "TRNB":
        tipo_tarifa = "Tarifa Residencial Normal Branca"
        print("\n\n")
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {tipo_tarifa} ")
        print(
            f"O valor da conta é : R$ {valor_conta:.2f} com pagamento no {forma_pagamento} ")
    else:
        print("Tipo de tarifa inválida")


def main():
    """função principal do programa"""
    while True:  # Loop para continuar ou não o programa
        nome_cliente = obter_nome_cliente()
        consumo_total = obter_consumo_total()
        tipo_tarifa = obter_tipo_tarifa()
        forma_pagamento = escolha_forma_pagamento()
        valor_conta = calcular_consumo(
            consumo_total, tipo_tarifa, forma_pagamento)
        impressao_conta(tipo_tarifa, nome_cliente,
                        forma_pagamento, valor_conta)
        continuar = input("Deseja continuar? [S/N]: ")
        if continuar.upper() == "N":
            print("Programa encerrado")
            break
        else:
            continue


if __name__ == "__main__":
    main()
