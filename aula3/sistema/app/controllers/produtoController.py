from ..models.produto import Produto
from ..database.database import BaseDeDados

class produtoController:
    
    def __init__(self):
        # Conexão com p Banco
        self.db = BaseDeDados()

    def criar_Produto(self, nome, preco):
        # Criar produto ( produto )
        novo_produto = Produto(nome, preco)
        dict_produto = {
            "nome": novo_produto.nome,
            "preco": novo_produto.preco,
        }
        self.db.adicionar_produto(dict_produto)
        print("Produto cadastrado com sucesso!")

    def listar_produtos(self):
        """
        Retorna [] com todos os produtos
        """
        return self.db.listar_produtos()
