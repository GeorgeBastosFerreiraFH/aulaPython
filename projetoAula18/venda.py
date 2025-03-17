import sqlite3

class Vendas:
    def __init__(self, db_file="estoque_loja.db"):
        self.conexao = sqlite3.connect(db_file)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        """Cria a tabela 'vendas' se ela ainda não existir."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER,
            id_produto INTEGER,
            qntd_vendida INTEGER,
            data_venda DATE,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
        )
        """)
        self.conexao.commit()

    def registrar_venda(self, id_cliente, id_produto, qntd_vendida, data_venda):
        """Registra uma nova venda na tabela 'vendas'."""
        try:
            self.cursor.execute("""
            INSERT INTO vendas(id_cliente, id_produto, qntd_vendida, data_venda)
            VALUES (?, ?, ?, ?)
            """, (id_cliente, id_produto, qntd_vendida, data_venda))
            self.conexao.commit()
            print("Venda registrada com sucesso!")
        except Exception as e:
            print(f"Erro ao registrar venda: {e}")

    def ver_vendas(self):
        """Exibe todas as vendas registradas na tabela 'vendas'."""
        try:
            self.cursor.execute("SELECT * FROM vendas")
            vendas = self.cursor.fetchall()
            for venda in vendas:
                print(venda)
        except Exception as e:
            print(f"Erro ao listar vendas: {e}")

    def deletar_venda(self, id):
        """Deleta uma venda da tabela 'vendas' pelo ID."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM vendas WHERE id = ?", (id,))
            resultado = self.cursor.fetchone()[0]
            if resultado == 0:
                print("Venda não encontrada!")
            else:
                self.cursor.execute("DELETE FROM vendas WHERE id = ?", (id,))
                self.conexao.commit()
                print("Venda deletada com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar venda: {e}")

    def editar_venda(self, id_cliente, id_produto, qntd_vendida, data_venda, id):
        """Edita os dados de uma venda na tabela 'vendas' pelo ID."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM vendas WHERE id = ?", (id,))
            resultado = self.cursor.fetchone()[0]
            if resultado == 0:
                print("Venda não encontrada!")
            else:
                self.cursor.execute("""
                UPDATE vendas SET id_cliente = ?, id_produto = ?, qntd_vendida = ?, data_venda = ? WHERE id = ?
                """, (id_cliente, id_produto, qntd_vendida, data_venda, id))
                self.conexao.commit()
                print("Venda editada com sucesso!")
        except Exception as e:
            print(f"Erro ao editar venda: {e}")

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        self.cursor.close()
        self.conexao.close()