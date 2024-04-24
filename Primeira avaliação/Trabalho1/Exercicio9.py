import math

# Obtenha as coordenadas do usuário
x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calcule a distância usando a fórmula da distância
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Imprima o resultado
print("A distância entre os dois pontos é:", round(distancia,2))
