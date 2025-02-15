"""
    Sistema de descontos de veiculos
    solicite o nome do veiculo
    e o preo do veiculo
    Se o preco > 80k => 60% de desconto
    Se o preco > 50k => 30% de desconto
    Se o preco < 30k => nao tem desconto
"""

print("Digite o nome do veiculo")
name = input()

print("Digite o preco do veiculo")
price = float(input())

print("nome do carro:", name)
print("Valor sem desconto: R$", price)

if price < 50000:
    print("Voce não tem direito a  discontos")

elif price > 80000:
    desconto = (price * 60) / 100
    print("Voce tem direito a um disconto de 60%")
    print("Valor com desconto: R$", desconto)
    
elif price > 50000:
    desconto = (price * 30) / 100
    print("Voce tem direito a um disconto de 30%")
    print("Valor com desconto: R$", desconto)
