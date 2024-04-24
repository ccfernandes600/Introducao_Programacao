# Solicite ao usuário que digite três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcule a média
media = (nota1 + nota2 + nota3) / 3

# Imprima o resultado
print("A média das notas é:", round(media,2))