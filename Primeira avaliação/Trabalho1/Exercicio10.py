# Pedir ao usuário para inserir as coordenadas dos dois pontos
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calcular o coeficiente angular (m)
m = (y2 - y1) / (x2 - x1)

# Calcular o coeficiente linear (b)
b = y1 - m * x1

# Imprimir a equação da reta
print(f"A equação da reta que passa pelos pontos ({x1}, {y1}) e ({x2}, {y2}) é: y = {m}x + {b}")