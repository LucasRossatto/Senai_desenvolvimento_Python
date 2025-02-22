from app.controllers.clienteController import clienteController
from app.controllers.produtoController import produtoController


def exibir_menu():
    print("\n==== Menu ====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("3 - Cadastrar Produto")
    print("4 - Listar Produtos")
    print("9 - Sair do Sistema")


def main():
    controlCliente = clienteController()
    controlProduto = produtoController()
    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do Cliene: ")
            email = input("Email: ")
            idade = input("Idade do Cliene: ")
            controlCliente.criar_cliente(nome, email, idade)

        elif opc == "2":
            clientes = controlCliente.listar_clientes()
            # index -> Posicao atual do cliente
            # __str__ -> cliente Cliente(nome="", email="", idade="")
            for index, cliente in enumerate(clientes, 1):
                print(f"{index}. {cliente}")

        elif opc == "3":
            nome = input("Nome do Produto: ")
            preco = input("Preço: ")
            controlProduto.criar_Produto(nome, preco)

        elif opc == "4":
            produtos = controlProduto.listar_produtos()
            for index, produto in enumerate(produtos, 1):
                print(f"{index}. {produto}")

        elif opc == "0":
            print("Saindo do sistema... ")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
