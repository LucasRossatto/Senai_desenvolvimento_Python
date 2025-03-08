import mysql.connector
from config import Config


class ProdutoModel:

    def __init__(self):
        self.config = Config()
        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB,
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_all_produtos(self):
        query = "SELECT * FROM produtos"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insert_produtos(self, nome, preco):
        query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
        self.cursor.execute(query, (nome, preco))
        self.connection.commit()
        return self.cursor.lastrowid

    def get_produto_by_id(self, produto_id):
        query = "SELECT * WHERE id = %s"
        self.cursor.execute(query, produto_id)
        return self.cursor.fedtchone()

    def delete_produto_by_id(self, produto_id):
        query = "DELETE FROM produtos WHERE id = %s"
        self.cursor.execute(query, produto_id)
        self.connection.commit()
        return self.cursor.rowcount

    def update_produto_by_id(self, produto_id, nome, preco):
        query = "UPDATE produtos SET nome = %s, preco = %s WHERE id = %s"
        self.cursor.execute(query, (nome, preco, produto_id))
        self.connection.commit()
        return self.cursor.rowcount

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
