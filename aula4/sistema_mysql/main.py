from src.controller import produto_controller

def exibir_menu():
    print("\nMercado Preso")
    print("\n==== Menu ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    #print("3 - Atualizar Produto")
    #print("4 - Deletar Produto")
    #print("5 - Buscar Produto único")
    print("9 - Sair")

def listar_produtos():
    print("\n--- Lista de Produtos ---")
    produtos = produto_controller.listar_produtos()
    if produtos:
         for produto in produtos:
            print(produto)
            print(f"ID: {produtos['id']}, Nome: {produto['nome']}, Preco {produto['preco']}")
    else:
            print("Não existe produtos cadastrados")
    
def cadastrar_produto():
    print("\n --- Cadastrar Produto ---")
    nome = input("Digite o nome: ")
    preco =  input("Digite o preço:")
    novo_id = produto_controller.cadastrar_produtos(nome, preco)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}.")

def main():
    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc =="2":
            listar_produtos()
        elif opc =="9":
            print("Saindo do sistema...")
            # sys.exit(0)


if __name__ == "__main__":
    main()