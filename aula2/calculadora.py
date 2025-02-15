def menu():
    print("==========================")
    print("Menu da Calculadora")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("9 - Sair")
    print("==========================")


def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 * n2


def verificar_opcao(opcao):

    if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado: {somar(n1, n2)}")

    elif opcao == 2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado: {subtrair(n1, n2)}")

    elif opcao == 3:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))    
        print(f"Resultado: {multiplicar(n1, n2)}")

    elif opcao == 4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado: {dividir(n1, n2)}")

    elif opcao == 9:
        print("Saindo...")
        return False


def calculadora():
    while True:
        menu()
        opcao = int(input("Escolha uma opção: "))
        verificar_opcao(opcao)


calculadora()
