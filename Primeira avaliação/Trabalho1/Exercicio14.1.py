import numpy as np

import matplotlib.pyplot as plt

def encontrar_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + np.sqrt(delta)) / (2*a)
        x2 = (-b - np.sqrt(delta)) / (2*a)
        return x1, x2

def plotar_grafico(a, b, c):
    x = np.linspace(-10, 10, 100)
    y = a*x**2 + b*x + c

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico da Equação Quadrática')
    plt.legend(['Equação: {}x^2 + {}x + {}'.format(a, b, c)])
    plt.grid(True)
    plt.show()

# Solicitar os coeficientes ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Encontrar as raízes e plotar o gráfico
raizes = encontrar_raizes(a, b, c)
if raizes is None:
    print("A equação não possui raízes reais.")
else:
    print("Raízes encontradas:", raizes)
    plotar_grafico(a, b, c)