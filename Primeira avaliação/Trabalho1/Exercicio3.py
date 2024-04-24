# Solicita ao usuário para inserir três valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

# Verifica qual é o maior valor
maior_valor = max(valor1, valor2, valor3)

# Imprime o resultado
print("O maior valor é:", maior_valor)