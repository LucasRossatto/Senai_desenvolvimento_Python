from src.controller import produto_controller


def exibir_menu():
    print("\nBem vindo ao Mercado Preso")
    print("\n==== Menu ====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produto")
    print("3 - Atualizar Produto")
    # print("4 - Deletar Produto")
    # print("5 - Buscar Produto único")
    print("9 - Sair")


def listar_produtos():
    print("\n--- Lista de Produtos ---")
    
    produtos = produto_controller.listar_produtos()
    
    if produtos:
        for produto in produtos:
            print(f"Produto {produto['id']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
    else:
        print("Não existem produtos cadastrados.")


def cadastrar_produto():
    print("\n --- Cadastrar Produto ---")
    nome = input("Digite o nome: ")
    preco = input("Digite o preço:")
    novo_id = produto_controller.cadastrar_produtos(nome, preco)
    print(f"Produto cadastrado com sucesso com o novo ID {novo_id}.")

  
def atualizar_produto():
    print("\n --- Atulizar Produto ---")
    produto_id = int(input("Digite o ID do produto: "))
    novoNome = input("Digite o novo nome: ")
    novoPreco = input("Digite o novo preço:")
    linhas = produto_controller.atualizar_produto(produto_id, novoNome, novoPreco)
    if linhas > 0:
        print("Produto atulizado com sucesso")
    else:
        print("Nenhum produto foi atualizado")


def main():
    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            atualizar_produto()
        elif opc == "9":
            print("Saindo do sistema...")
            # sys.exit(0)


if __name__ == "__main__":
    main()
