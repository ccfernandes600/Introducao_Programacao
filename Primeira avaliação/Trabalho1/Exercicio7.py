def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Digite um número: "))
if is_prime(number):
    print(f"{number} é um número primo.")
else:
    print(f"{number} não é um número primo.")