


def celsius_para(temp_celsius):
    fahrenheit=(temp_celsius * 9/5) + 32  
    kelvin=temp_celsius + 273.15
    temp={
        "Fahrenheit": fahrenheit,
        "Kelvin": kelvin,
    }
    return temp

def fahrenheit_para(temp_fahrenheit):
    celsius=(temp_fahrenheit - 32) * 5/9
    kelvin= (temp_fahrenheit - 32) * 5/9 + 273.15
    temp={
        "Celsius": celsius,
        "Kelvin": kelvin,
    }
    return temp

def kelvin_para(temp_kelvin):
    celsius=temp_kelvin - 273.15
    fahrenheit=(temp_kelvin - 273.15) * 9/5 + 32
    temp={
        "Fahrenheit": fahrenheit,
        "Celsius": celsius,
    }
    return temp

while True:
    print("""\n
    Digite 1 para Calcular as conversões de unidades  de Temperatura \n
    Digite 2 para Calcukar as conbersões de unidades de volume \n
    Digite 3 para .......................................................\n
    Digite 4 para........................................................\n
    Digite 5 para.......................................................\n
    Digite 6 para.......................................................\n
    Digite 7 para Sair   
          """)
    tecla=input("Entre com valor numérico de acordo com as opções acima:")
    if tecla== "1":
      
        while True:
            print("Escolha a conversão desejada:")
            print("1. Celsius para Fahrenheit e Kelvin")
            print("2. Fahrenheit para Celsius e Kelvin")
            print("3. Kelvin para Celsius e Fahrenheit")
            print("4. para voltar ao menu Principal")

            escolha = input("Digite o número correspondente: ")

            if escolha == '1':
                temp_c = float(input("Digite a temperatura em Celsius: "))
                temp = celsius_para(temp_c)
                # Arredondando o valor da temperatura em Celsius
                temp["Fahrenheit"] = round(temp["Fahrenheit"], 2)
                temp["Kelvin"] = round(temp["Kelvin"], 2)
                print(f"Temperaturas Calculadas São : {temp}")
            elif escolha == '2':
                temp_f = float(input("Digite a temperatura em Fahrenheit: "))
                temp = fahrenheit_para(temp_f)
                # Arredondando o valor da temperatura em Fahrenheit
                temp["Celsius"] = round(temp["Celsius"], 2)
                temp["Kelvin"] = round(temp["Kelvin"], 2)
                print(f"Temperatura Calculadas São :  {temp}")
            elif escolha == '3':
                temp_k = float(input("Digite a temperatura em Kelvin: "))
                temp = kelvin_para(temp_k)
                # Arredondando o valor da temperatura em Kelvin
                temp["Fahrenheit"] = round(temp["Fahrenheit"], 2)
                temp["Celsius"] = round(temp["Celsius"], 2)
                print(f"Temperatura Calculadas São :  {temp}")
            elif escolha == '4':
                print("Voltando ao  menu principal...")
                break
            else:
                print("Escolha inválida. Por favor, escolha uma opção de 1 a 4.")
            print()
            print()
            print()
    elif tecla =="7":
        print("Programa finalizado com sucesso")
        break
    else:
        print("Escolha inválida. Por favor, escolha uma opção de 1 a 7.")
        