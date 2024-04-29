
""" Progrma para calcular o valor da conta de energia elétrica da Equatorial-MA da primeira 
avaliação da disciplina de Programação do curso de Engenharia Elétrica da UFMA
"""
# Autor: Claudio Fernandes
# Data: 12/04/2024


# Declaração de Constantes

PIX = 0.0
DEBITO = 0.02  # TAXA DE 2%
CREDITO = 0.05  # TAXA DE 5%

# Tarifa Residencial Baixa Renda
TARIFA_30K = 0.23033  # Tarifa (R$/kWh)
TARIFA_31_100K = 0.39485  # Tarifa (R$/kWh)
TARIFA_101_200K = 0.59227  # Tarifa (R$/kWh)
TARIFA_ACIMA_220K = 0.65808  # Tarifa (R$/kWh)

# Tarifa Residencial Normal Convencional
TARIFA_CONVENCIONAL = 0.71881  # Tarifa (R$/kWh)

# Tarifa Residencial Normal Branca
TARIFA_PONTA = 1.5968  # Tarifa (R$/kWh)
TARIFA_INTERMEDIARIO = 1.01266  # Tarifa (R$/kWh)
TARIFA_FORA_PONTA = 0.57891  # Tarifa (R$/kWh)

# Menu de entrada do nome do  Cliente clontrolada por Loop infinito
while True:
    print("\n\n\nCalcule o valor da sus conta Equatorial-MA\n\n\n")
    nome_cliente = input("Entre com o nome do consumidor:  ")
    print("""MENU:
          
    [TBR] - Tarifa Baixa Renda
    
    [TRNC] - Tarifa Residencial Normal Convencional
    
    [TRNB] - Tarifa Residencial Normal Branca\n\n""")
    while True:
        TIPO_TARIFA = input(
            "Entre com um das opções \"TBR\",\"TRNC\" ou \"TRNB\" :")
        TIPO_TARIFA = TIPO_TARIFA.upper()
        if TIPO_TARIFA == "TBR" or TIPO_TARIFA == "TRNC" or TIPO_TARIFA == "TRNB":
            break
        else:
            print("Opção de tarifa inválida")
            continue

        # Entrada de dados
    if TIPO_TARIFA == "TBR":
        consumo_total = float(
            input("Entre com o valor de kWh consumido no mês: "))
        CONSUMO_30K = 0
        CONSUMO_31_100K = 0
        CONSUMO_101_220K = 0
        CONSUMO_ACIMA_220K = 0
        if consumo_total <= 30:
            CONSUMO_30K = consumo_total
        elif consumo_total > 30 and consumo_total <= 100:
            CONSUMO_30K = 30
            CONSUMO_31_100K = consumo_total - 30
        elif consumo_total > 100 and consumo_total <= 220:
            CONSUMO_30K = 30
            CONSUMO_31_100K = 70
            CONSUMO_101_220K = consumo_total - 100
        else:
            CONSUMO_30K = 30
            CONSUMO_31_100K = 70
            CONSUMO_101_220K = 120
            CONSUMO_ACIMA_220K = consumo_total - 220

        # Calculo do consumo Baixa Renda C
        VALOR_CONSUMO_30K = CONSUMO_30K * TARIFA_30K
        VALOR_CONSUMO_31_100K = CONSUMO_31_100K * TARIFA_31_100K
        VALOR_CONSUMO_101_220K = CONSUMO_101_220K * TARIFA_101_200K
        VALOR_CONSUMO_ACIMA_220K = CONSUMO_ACIMA_220K * TARIFA_ACIMA_220K
    elif TIPO_TARIFA == "TRNC":
        consumo_convencional = float(
            input("Entre com valor de kWh consumido no mês: "))
        valor_consumo = consumo_convencional * TARIFA_CONVENCIONAL
    elif TIPO_TARIFA == "TRNB":
        consumo_total = float(
            input("Entre com o valor de kWh consumido no mês: "))
        consumo_ponta = consumo_total * 0.17  # 17% do consumo total
        consumo_intermediario = consumo_total * 0.25  # 25% do consumo de ponta
        consumo_fora_ponta = consumo_total * 0.58  # 58% do consumo total
        # Calculo consumo Normal
        VALOR_CONSUMO_PONTA = consumo_ponta * TARIFA_PONTA
        VALOR_CONSUMO_INTERMEDIARIO = consumo_intermediario * TARIFA_INTERMEDIARIO
        VALOR_CONSUMO_FORA_PONTA = consumo_fora_ponta * TARIFA_FORA_PONTA

    # Escolha da for de pagamento
    # Menu de entrada da forma de pagamento  clontrolada por Loop infinito

    print("Escolha a forma de Pagamento\n\n\n")
    print("""MENU:
    [P] - Pagamento com PIX")
    
    [D] - Pagamento com Cartão de Débito com juros de 2%")
    
    [C] - Pagamento com Cartão de Crédito com juros de 5%\n\n""")
    while True:
        FORMA_PAGAMENTO = input("Entre com \"P\" , \"D\" ou \"C\" : ")
        FORMA_PAGAMENTO = FORMA_PAGAMENTO.upper()
        if FORMA_PAGAMENTO == "P" or FORMA_PAGAMENTO == "D" or FORMA_PAGAMENTO == "C":
            break
        else:
            print("Opção de pagamento inválida")
            continue

    # Calculo da Conta de Energia consumida
    if FORMA_PAGAMENTO == "P":
        VALOR_CONSUMO_30K_CONSUMO_30K = 0
        VALOR_CONSUMO_31_100K = 0
        VALOR_CONSUMO_101_220K = 0
        VALOR_CONSUMO_ACIMA_220K = 0

        FORMA_PAGAMENTO = "PIX"
        if TIPO_TARIFA == "TBR":
            VALOR_CONTA = VALOR_CONSUMO_30K + VALOR_CONSUMO_31_100K + \
                VALOR_CONSUMO_101_220K + VALOR_CONSUMO_ACIMA_220K
            VALOR_CONTA = VALOR_CONTA + VALOR_CONTA*PIX
        elif TIPO_TARIFA == "TRNC":
            FORMA_PAGAMENTO = "PIX"
            VALOR_CONTA = valor_consumo + valor_consumo*PIX
        elif TIPO_TARIFA == "TRNB":
            FORMA_PAGAMENTO = "PIX"
            VALOR_CONSUMO_PONTA = 0
            VALOR_CONSUMO_INTERMEDIARIO = 0
            VALOR_CONSUMO_FORA_PONTA = 0
            VALOR_CONTA = VALOR_CONSUMO_PONTA + \
                VALOR_CONSUMO_INTERMEDIARIO + VALOR_CONSUMO_FORA_PONTA
            VALOR_CONTA = VALOR_CONTA + VALOR_CONTA*PIX

    elif FORMA_PAGAMENTO == "D":
        FORMA_PAGAMENTO = "DÉBITO"
        VALOR_CONSUMO_30K = 0
        VALOR_CONSUMO_31_100K = 0
        VALOR_CONSUMO_101_220K = 0
        VALOR_CONSUMO_ACIMA_220K = 0
        if TIPO_TARIFA == "TBR":
            VALOR_CONTA = VALOR_CONSUMO_30K + VALOR_CONSUMO_31_100K + \
                VALOR_CONSUMO_101_220K + VALOR_CONSUMO_ACIMA_220K
            VALOR_CONTA = VALOR_CONTA + VALOR_CONTA*DEBITO
        elif TIPO_TARIFA == "TRNC":
            FORMA_PAGAMENTO = "DÉBITO"
            VALOR_CONTA = valor_consumo + valor_consumo*DEBITO
        elif TIPO_TARIFA == "TRNB":
            FORMA_PAGAMENTO = "DÉBITO"
            VALOR_CONSUMO_FORA_PONTA = VALOR_CONSUMO_INTERMEDIARIO
            VALOR_CONTA = VALOR_CONSUMO_PONTA + \
                VALOR_CONSUMO_INTERMEDIARIO + VALOR_CONSUMO_FORA_PONTA  # type: ignore
            VALOR_CONTA = VALOR_CONTA + VALOR_CONTA*DEBITO
    elif FORMA_PAGAMENTO == "C":
        FORMA_PAGAMENTO = "CRÉDITO"
        if TIPO_TARIFA == "TBR":
            VALOR_CONTA = VALOR_CONSUMO_30K + VALOR_CONSUMO_31_100K + \
                VALOR_CONSUMO_101_220K + VALOR_CONSUMO_ACIMA_220K  # type: ignore
            VALOR_CONTA = VALOR_CONTA + VALOR_CONTA*CREDITO
        elif TIPO_TARIFA == "TRNC":
            FORMA_PAGAMENTO = "CRÉDITO"
            VALOR_CONTA = valor_consumo + valor_consumo*CREDITO
        elif TIPO_TARIFA == "TRNB":
            FORMA_PAGAMENTO = "CRÉDITO"
            VALOR_CONTA = VALOR_CONSUMO_PONTA + \
                VALOR_CONSUMO_INTERMEDIARIO + VALOR_CONSUMO_FORA_PONTA  # type: ignore
            VALOR_CONTA = VALOR_CONTA + VALOR_CONTA*CREDITO

    # Impressão da conta
    if TIPO_TARIFA == "TBR":
        TIPO_TARIFA = "Tarifa Residencial Baixa Renda Convencional"
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {TIPO_TARIFA} ")
        print(
            f"O valor da conta é : R$ {VALOR_CONTA:.2f} com pagamento no {FORMA_PAGAMENTO}   ")

    elif TIPO_TARIFA == "TRNC":
        TIPO_TARIFA = "Tarifa Residencial Normal Convencional"
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {TIPO_TARIFA} ")
        print(
            f"O valor da conta é : R$ {VALOR_CONTA:.2f} com pagamento no {FORMA_PAGAMENTO}   ")

    elif TIPO_TARIFA == "TRNB":
        TIPO_TARIFA = "Tarifa Residencial Normal Branca"
        print(
            f"Impressão da conta do Consumidor {nome_cliente} com tarifa tipo {TIPO_TARIFA} ")
        print(
            f"O valor da conta é : R$ {VALOR_CONTA:.2f} com pagamento no {FORMA_PAGAMENTO} ")

        # Menu para verificar se o usuário deseja entrar com nova consulta o sair
    teste = input(
        "Digite \"S\" para sair ou qualquer outra tecla para continuar:  ")
    if teste == "S" or teste == "s":
        break
    else:
        continue
