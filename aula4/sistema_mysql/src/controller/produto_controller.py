from ..model.produto_model import ProdutoModel


def listar_produtos():
    model = ProdutoModel()
    produtos = model.get_all_produtos()
    model.close_connection()
    return produtos


def cadastrar_produtos(nome, preco):
    model = ProdutoModel()
    novo_id = model.insert_produtos(nome, preco)
    print(novo_id)
    model.close_connection()
    return novo_id


def atualizar_produto(produto_id, nome, preco):
    model = ProdutoModel()
    linhas_afetadas = model.update_produto_by_id(produto_id, nome, preco)
    model.close_connection()
    return linhas_afetadas


def remover_produto(produto_id):
    model = ProdutoModel()
    linhas_afetadas = model.delete_produto_by_id(produto_id)
    model.close_connection()
    return linhas_afetadas


def obter_produto(produto_id):
    model = ProdutoModel()
    produto = model.get_produto_by_id(produto_id)
    model.close_connection()
    return produto
