import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host="localhost",   
            user="root",        
            password="root",   
            database="pythonCrud" 
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None


import mysql.connector  

def criar_tabela():
    try:
        conn = conectar()
        if conn is None:
            print("Erro: Não foi possível conectar ao banco de dados.")
            return
        
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(100),
            idade INT
        )
        """)

        conn.commit()
        print("Tabela 'clientes' criada com sucesso.")
    except Exception as e:
        print(f"Erro ao criar a tabela: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
