# Numeros pares em intervalo

print("Digite um numero para ser o limite inicial")
limiteInicial = float(input())
print("Digite um numero para ser o fim do intervalo")
fimIntervalo = float(input())

for y in range(limiteInicial, fimIntervalo + 1):
    if y % 2 == 0:
        print("o Número par é: ", y)