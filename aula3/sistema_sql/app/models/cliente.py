from app.database.database import conectar


class Cliente:

    def __init__(self, nome, email, idade, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.idade = idade

    def salvar(self):
        """Cria ou atualiza um cliente no banco de dados."""
        try:
            conn = conectar()
            if conn is None:
                print("Erro: Não foi possível conectar ao banco de dados.")
                return

            cursor = conn.cursor()

            if self.id:
                cursor.execute(
                    """
                    UPDATE clientes SET nome = %s, email = %s, idade = %s WHERE id = %s
                    """,
                    (self.nome, self.email, self.idade, self.id),
                )
            else:
                cursor.execute(
                    """
                    INSERT INTO clientes (nome, email, idade) VALUES (%s, %s, %s)
                    """,
                    (self.nome, self.email, self.idade),
                )
                self.id = cursor.lastrowid  # Obtém o ID gerado após o INSERT

            conn.commit()

        except Exception as e:
            print(f"Erro ao criar/atualizar cliente: {e}")
        finally:
            if "cursor" in locals():
                cursor.close()
            if "conn" in locals():
                conn.close()

    @staticmethod
    def buscar_todos():
        """Busca todos os clientes no banco de dados."""
        try:
            conn = conectar()
            if conn is None:
                print("Erro: Não foi possível conectar ao banco de dados.")
                return []

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM clientes")
            clientes = []
            for row in cursor.fetchall():
                cliente = Cliente(row[1], row[2], row[3], row[0])
                clientes.append(cliente)

            return clientes

        except Exception as e:
            print(f"Erro ao buscar clientes: {e}")
            return []
        finally:
            if "cursor" in locals():
                cursor.close()
            if "conn" in locals():
                conn.close()

    @staticmethod
    def buscar_por_id(id):
        """Busca um cliente pelo ID no banco de dados."""
        try:
            conn = conectar()
            if conn is None:
                print("Erro: Não foi possível conectar ao banco de dados.")
                return None

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
            row = cursor.fetchone()

            if row:
                return Cliente(row[1], row[2], row[3], row[0])

            return None

        except Exception as e:
            print(f"Erro ao buscar cliente por ID: {e}")
            return None
        finally:
            if "cursor" in locals():
                cursor.close()
            if "conn" in locals():
                conn.close()

    def deletar(self):
        """Deleta um cliente do banco de dados."""
        try:
            conn = conectar()

            if conn is None:
                print("Erro: Não foi possível conectar ao banco de dados.")
                return False

            cursor = conn.cursor()

            cursor.execute("DELETE FROM clientes WHERE id = %s", (self.id,))
            conn.commit()

            return True

        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")
            return False
        finally:
            if "cursor" in locals():
                cursor.close()
            if "conn" in locals():
                conn.close()
