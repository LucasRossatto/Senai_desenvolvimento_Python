# Veirifcar se é impar ou par

print("Digite um número inteiro para saber se ele é impar ou par")
n = int(input())

resultado = n % 2

if resultado == 0:
    print("O número",n,"é par")
else:
    print("O número",n,"é impar")
