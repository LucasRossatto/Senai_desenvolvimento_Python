from app.controllers.clienteController import ClienteController
from app.database.database import criar_tabela

def exibir_menu():
    print("\n==== Menu ====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("3 - Atualizar Cliente")
    print("4 - Deletar Cliente")
    print("9 - Sair do Sistema")
    
def main():
    criar_tabela()
    controlCliente = ClienteController() 

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            while True:
                try:
                    idade = int(input("Idade: "))  
                    break
                except ValueError:
                    print("Erro: Digite um número válido para idade.")

            controlCliente.criar_cliente(nome, email, idade)
            print("Novo Cliente criado com sucesso!")

        elif opc == "2":
            clientes = controlCliente.listar_clientes() or []
            if not clientes:
                print("Nenhum cliente cadastrado.")
            else:
                for cliente in clientes:
                    print(f"ID: {cliente.id}, Nome: {cliente.nome}, Email: {cliente.email}, Idade: {cliente.idade}")

        elif opc == "3":
            while True:
                try:
                    id = int(input("ID do cliente: "))
                    break
                except ValueError:
                    print("Erro: Digite um número válido para o ID.")

            nome = input("Novo nome: ")
            email = input("Novo email: ")
            while True:
                try:
                    idade = int(input("Nova idade: "))  
                    break
                except ValueError:
                    print("Erro: Digite um número válido para a idade.")

            if controlCliente.atualizar_cliente(id, nome, email, idade):
                print("Cliente atualizado com sucesso!")
            else:
                print("Cliente não encontrado.")

        elif opc == "4":
            while True:
                try:
                    id = int(input("ID do cliente: "))
                    break
                except ValueError:
                    print("Erro: Digite um número válido para o ID.")

            if controlCliente.deletar_cliente(id):
                print("Cliente deletado com sucesso!")
            else:
                print("Cliente não encontrado.")

        elif opc == "9":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
