lado = float(input("Digite o valor do lado do quadrado: "))

if lado > 0:
    area = lado * lado
    print("A área do quadrado é:", area)
else:
    print("O valor do lado deve ser maior que zero.")