# -*- coding: utf-8 -*-
#
# Autor: Claudio Fernandes
# Data: 12/04/2024


# Declaração de Constantes

PIX = 0.0
DEBITO = 0.02  # TAXA DE 2%
CREDITO = 0.05  # TAXA DE 5%

# Tarifa Residencial Baixa Renda
TARIFA30k = 0.23033  # Tarifa (R$/kWh)
TARIFA31_100k = 0.39485  # Tarifa (R$/kWh)
TARIFA101_220k = 0.59227  # Tarifa (R$/kWh)
TARIFA_ACIMA_220k= 0.65808  # Tarifa (R$/kWh)

# Tarifa Residencial Normal Convencional
TARIFA_CONVENCIONAL = 0.71881  # Tarifa (R$/kWh)

# Tarifa Residencial Normal Branca
TARIFA_PONTA= 1.5968  # Tarifa (R$/kWh)
TARIFA_INTERMEDIARIO = 1.01266  # Tarifa (R$/kWh)
TARIFA_FORA_PONTA = 0.57891  # Tarifa (R$/kWh)

#Menu de entrada do nome do  Cliente clontrolada por Loop infinito
while True:
    print("\n\n\nCalcule o valor da sus conta Equatorial-MA\n\n\n")
    nome_cliente = input("Entre com o nome do consumidor:  ")
    print("""MENU:
          
    [TBR] - Tarifa Baixa Renda
    
    [TRNC] - Tarifa Residencial Normal Convencional
    
    [TRNB] - Tarifa Residencial Normal Branca\n\n""")
    while True:
        tipo_tarifa = input(
            "Entre com um das opções \"TBR\",\"TRNC\" ou \"TRNB\" :")
        tipo_tarifa = tipo_tarifa.upper()
        if tipo_tarifa == "TBR" or tipo_tarifa == "TRNC" or tipo_tarifa == "TRNB":
            break
        else:
            print("Opção de tarifa inválida")
            continue

        # Entrada de dados
    if tipo_tarifa == "TBR":
        consumo_total = float(input("Entre com o valor de kWh consumido no mês: "))
        consumo30K = 0
        consumo31_100K = 0
        consumo101_220K = 0
        consumo_acima_220K = 0
        if consumo_total <= 30:
            consumo30K = consumo_total
        elif consumo_total > 30 and consumo_total <= 100:
            consumo30K = 30
            consumo31_100K = consumo_total - 30
        elif consumo_total > 100 and consumo_total <= 220:
            consumo30K = 30
            consumo31_100K = 70
            consumo101_220K = consumo_total - 100
        else:
            consumo30K = 30
            consumo31_100K = 70
            consumo101_220K = 120
            consumo_acima_220K = consumo_total - 220
        

        # Calculo do consumo Baixa Renda C
        valor_consumo30K = consumo30K * TARIFA30k
        valor_consumo31_100K = consumo31_100K * TARIFA31_100k
        valor_consumo101_220K = consumo101_220K * TARIFA101_220k
        valor_consumo_acima_220K = consumo_acima_220K * TARIFA_ACIMA_220k
    elif tipo_tarifa == "TRNC":
        consumo_convencional = float(
            input("Entre com valor de kWh consumido no mês: "))
        valor_consumo = consumo_convencional * TARIFA_CONVENCIONAL
    elif tipo_tarifa == "TRNB":
        consumo_total = float(input("Entre com o valor de kWh consumido no mês: "))
        consumo_ponta = consumo_total * 0.17 # 17% do consumo total
        consumo_intermediário = consumo_total * 0.25 # 25% do consumo de ponta
        consumo_fora_ponta = consumo_total * 0.58 # 58% do consumo total
        # Calculo consumo Normal
        valor_consumo_ponta = consumo_ponta * TARIFA_PONTA
        valor_consumo_intermediário = consumo_intermediário * TARIFA_INTERMEDIARIO
        valor_consumo_fora_ponta = consumo_fora_ponta * TARIFA_FORA_PONTA

    # Escolha da for de pagamento
    #Menu de entrada da forma de pagamento  clontrolada por Loop infinito

    print("Escolha a forma de Pagamento\n\n\n")
    print("""MENU:
    [P] - Pagamento com PIX")
    
    [D] - Pagamento com Cartão de Débito com juros de 2%")
    
    [C] - Pagamento com Cartão de Crédito com juros de 5%\n\n""")
    while True:
        forma_pagamento = input("Entre com \"P\" , \"D\" ou \"C\" : ")
        forma_pagamento = forma_pagamento.upper()
        if forma_pagamento.upper() == "P" or forma_pagamento.upper() == "D" or forma_pagamento.upper() == "C":
            break
        else:
            print("Opção de pagamento inválida")
            continue

    # Calculo da Conta de Energia consumida
    if forma_pagamento == "P":
        valor_consumo30K = 0
        valor_consumo31_100K = 0
        valor_consumo101_220K = 0
        valor_consumo_acima_220K = 0

        forma_pagamento = "PIX"
        if tipo_tarifa == "TBR":
            valor_conta = valor_consumo30K + valor_consumo31_100K + valor_consumo101_220K + valor_consumo_acima_220K
            valor_conta = valor_conta + valor_conta*PIX
        elif tipo_tarifa == "TRNC":
            forma_pagamento = "PIX"
            valor_conta = valor_consumo + valor_consumo*PIX
        elif tipo_tarifa == "TRNB":
            forma_pagamento = "PIX"
            valor_consumo_ponta = 0
            valor_consumo_intermediário = 0
            valor_consumo_fora_ponta = 0
            valor_conta = valor_consumo_ponta + valor_consumo_intermediário + valor_consumo_fora_ponta
            valor_conta = valor_conta + valor_conta*PIX

    elif forma_pagamento == "D":
        forma_pagamento = "DÉBITO"
        valor_consumo30K = 0
        valor_consumo31_100K = 0
        valor_consumo101_220K = 0
        valor_consumo_acima_220K = 0
        if tipo_tarifa == "TBR":
            valor_conta = valor_consumo30K + valor_consumo31_100K + \
                valor_consumo101_220K + valor_consumo_acima_220K
            valor_conta = valor_conta + valor_conta*DEBITO
        elif tipo_tarifa == "TRNC":
            forma_pagamento = "DÉBITO"
            valor_conta = valor_consumo + valor_consumo*DEBITO
        elif tipo_tarifa == "TRNB":
            forma_pagamento = "DÉBITO"
            valor_consumo_fora_ponta = valor_consumo_intermediário
            valor_conta = valor_consumo_ponta + \
                valor_consumo_intermediário + valor_consumo_fora_ponta # type: ignore
            valor_conta = valor_conta + valor_conta*DEBITO
    elif forma_pagamento == "C":
        forma_pagamento = "CRÉDITO"
        if tipo_tarifa == "TBR":
            valor_conta = valor_consumo30K + valor_consumo31_100K + \ # type: ignore
                valor_consumo101_220K + valor_consumo_acima_220K # type: ignore
            valor_conta = valor_conta + valor_conta*CREDITO
        elif tipo_tarifa == "TRNC":
            forma_pagamento = "CRÉDITO"
            valor_conta = valor_consumo + valor_consumo*CREDITO
        elif tipo_tarifa == "TRNB":
            forma_pagamento = "CRÉDITO"
            valor_conta = valor_consumo_ponta + \
                valor_consumo_intermediário + valor_consumo_fora_ponta # type: ignore
            valor_conta = valor_conta + valor_conta*CREDITO

    # Impressão da conta
    if tipo_tarifa == "TBR":
        tipo_tarifa = "Tarifa Residencial Baixa Renda Convencional"
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {tipo_tarifa} ")
        print(
            f"O valor da conta é : R$ {valor_conta:.2f} com pagamento no {forma_pagamento}   ")

    elif tipo_tarifa == "TRNC":
        tipo_tarifa = "Tarifa Residencial Normal Convencional"
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {tipo_tarifa} ")
        print(
            f"O valor da conta é : R$ {valor_conta:.2f} com pagamento no {forma_pagamento}   ")

    elif tipo_tarifa == "TRNB":
        tipo_tarifa = "Tarifa Residencial Normal Branca"
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {tipo_tarifa} ")
        print(
            f"O valor da conta é : R$ {valor_conta:.2f} com pagamento no {forma_pagamento} ")

        # Menu para verificar se o usuário deseja entrar com nova consulta o sair
    teste = input(
        "Digite \"S\" para sair ou qualquer outra tecla para continuar:  ")
    if teste == "S" or teste == "s":
        break
    else:
        continue
