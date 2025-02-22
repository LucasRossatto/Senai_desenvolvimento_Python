from ..models.cliente import Cliente
from ..database.database import BaseDeDados

class clienteController:

    def __init__(self):
        # Conexão com p Banco
        self.db = BaseDeDados()

    def criar_cliente(self, nome, email, idade):
        # Criar obejto ( cliente )
        novo_cliente = Cliente(nome, email, idade)
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade,
        }
        self.db.adicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")

    def listar_clientes(self):
        """
        Retorna [] com todos os clientes
        """
        return self.db.listar_clientes()
