import json
from pathlib import Path

class BaseDeDados:

    def __init__(self, arquivo_db="banco.json"):
        self.arquivo_db = arquivo_db
        self.dados = {"clientes": [], "produtos": []}
        self._carregar()

    def _carregar(self):
        """
        Carrega dados do arquivo JSON, se existir.
        caso não exista, inicia com dados vazio
        """
        caminho = Path(self.arquivo_db)
        if caminho.is_file():
            with open(caminho, "r", encoding="utf-8") as data:
                self.dados = json.load(data)
        else:
            self._salvar()

    def _salvar(self):
        """
        Salvar o conteuo de self dados no modo JSON
        """
        with open(self.arquivo_db, "w", encoding="utf-8") as data:
            json.dump(self.dados, data, ensure_ascii=False, indent=4)

    def adicionar_cliente(self, cliente_dict):
        self.dados["clientes"].append(cliente_dict)
        self._salvar()

    def listar_clientes(self):
        return self.dados["clientes"]
    
    def adicionar_produto(self, produto_dict):
        self.dados["produtos"].append(produto_dict)
        self._salvar()

    def listar_produtos(self):
        return self.dados["produtos"]
