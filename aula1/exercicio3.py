# Calculadora de Imc
print("Bem vindo a sua calculadora de Indice de massa corporal ( IMC )")
print("Digite seu peso em kg's")
peso = float(input())
print("Digite sua altura em m's")
altura = float(input())

imc = peso / (altura * 2)
print("Seu IMC é:")
if imc < 18.5:
    print("Abaixo do normal")
elif imc < 24.9:
    print("Normal")
elif imc < 29.9:
    print("SobrePeso")
elif imc < 34.9:
    print("Obesidade Grau I")
elif imc < 39.9:
    print("Obesidade Grau II")
elif imc > 40:
    print("Obesidade III")