import sqlite3

class Clientes:
    def __init__(self, db_file="estoque_loja.db"):
        self.conexao = sqlite3.connect(db_file)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            endereco TEXT
        )
        """)
        self.conexao.commit()

    def adicionar_cliente(self, nome, email, endereco):
        try:
            self.cursor.execute("""
            INSERT INTO clientes(nome, email, endereco)
            VALUES (?, ?, ?)
            """, (nome, email, endereco))
            self.conexao.commit()
            print("Cliente adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar cliente: {e}")

    def ver_clientes(self):
        try:
            self.cursor.execute("SELECT * FROM clientes")
            clientes = self.cursor.fetchall()
            if not clientes:
                print("Nenhum cliente cadastrado!")
            else:
                print("\n--- Lista de Clientes ---")
                for cliente in clientes:
                    id_cliente, nome, email, endereco = cliente
                    print("\n---------------------------")
                    print(f"ID do cliente: {id_cliente}")
                    print(f"Nome: {nome}")
                    print(f"Email: {email}")
                    print(f"Endereço: {endereco}")
                    print("---------------------------")
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")

    def deletar_cliente(self, id):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM clientes")
            total = self.cursor.fetchone()[0]
            if total == 0:
                print("Nenhum cliente cadastrado!")
                return

            self.cursor.execute("SELECT COUNT(*) FROM clientes WHERE id_cliente = ?", (id,))
            resultado = self.cursor.fetchone()[0]
            if resultado == 0:
                print("Cliente não encontrado!")
            else:
                self.cursor.execute("DELETE FROM clientes WHERE id_cliente = ?", (id,))
                self.conexao.commit()
                print("Cliente deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar cliente: {e}")

    def editar_cliente(self, nome, email, endereco, id):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM clientes")
            total = self.cursor.fetchone()[0]
            if total == 0:
                print("Nenhum cliente cadastrado!")
                return

            self.cursor.execute("SELECT COUNT(*) FROM clientes WHERE id_cliente = ?", (id,))
            resultado = self.cursor.fetchone()[0]
            if resultado == 0:
                print("Cliente não encontrado!")
            else:
                self.cursor.execute("""
                    UPDATE clientes
                    SET nome = ?, email = ?, endereco = ?
                    WHERE id_cliente = ?
                """, (nome, email, endereco, id))
                self.conexao.commit()
                print("Cliente editado com sucesso!")
        except Exception as e:
            print(f"Erro ao editar cliente: {e}")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
