"""
    Calcular bhaskara
    Delta = b2 - 4 * a * c
    Bhaskara = (-b +- srqt) / (s*a)
"""

import math 

print("Digite o valor de A")
a = float(input())
print("Digite o valor de B")
b = float(input())
print("Digite o valor de C")
c = float(input())

delta  = b**2 - 4 * ( a * c )
print("valor de delta:",delta)

raizDeDelta = math.sqrt(delta)
print("raiza quadrada de delta:",raizDeDelta)
x1  = (-b + raizDeDelta) / (2 * a)
x2 = (-b - raizDeDelta) / (2 * a)
print("x1: ",x1)
print("x2: ",x1)
