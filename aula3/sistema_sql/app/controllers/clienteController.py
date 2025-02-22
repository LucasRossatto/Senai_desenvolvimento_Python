from app.models.cliente import Cliente 

class ClienteController:

    @staticmethod
    def criar_cliente(nome, email, idade):
        try:
            cliente = Cliente(nome, email, idade)
            cliente.salvar()  
            return cliente
        except Exception as e:
            print(f"Erro ao criar cliente: {e}")
            return None

    @staticmethod
    def listar_clientes():
        try:
            return Cliente.buscar_todos() or []  
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")
            return []

    @staticmethod
    def atualizar_cliente(id, nome, email, idade):
        """Atualiza um usuário existente."""
        try:
            cliente = Cliente.buscar_por_id(id)
            if cliente:
                cliente.nome = nome
                cliente.email = email
                cliente.idade = idade
                cliente.salvar()
                return cliente
            return None
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            return None

    @staticmethod
    def deletar_cliente(id):
        """Deleta um usuário."""
        try:
            cliente = Cliente.buscar_por_id(id)
            if cliente:
                cliente.deletar()  
                return True
            return False
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
            return False
