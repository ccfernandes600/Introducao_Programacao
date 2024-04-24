import math

# Obter entrada do usuário
ponto_x = float(input("Digite a coordenada x do ponto: "))
ponto_y = float(input("Digite a coordenada y do ponto: "))
centro_x = float(input("Digite a coordenada x do centro do círculo: "))
centro_y = float(input("Digite a coordenada y do centro do círculo: "))
raio = float(input("Digite o raio do círculo: "))

# Calcular a distância entre o ponto e o centro do círculo
distancia = math.sqrt((ponto_x - centro_x) ** 2 + (ponto_y - centro_y) ** 2)

# Verificar se o ponto está dentro do círculo
if distancia <= raio:
    print("O ponto está dentro do círculo.")
else:
    print("O ponto está fora do círculo.")
