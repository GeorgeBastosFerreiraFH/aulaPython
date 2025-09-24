import sqlite3
from datetime import datetime

class Vendas:
    def __init__(self, db_file="estoque_loja.db"):
        self.conexao = sqlite3.connect(db_file)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER,
            id_produto INTEGER,
            qntd_vendida INTEGER,
            data_venda DATETIME,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
            FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
        )
        """)
        self.conexao.commit()

    def registrar_venda(self, id_cliente, id_produto, qntd_vendida):
        try:
            self.cursor.execute("SELECT qntd_estoque FROM produtos WHERE id_produto = ?", (id_produto,))
            produto = self.cursor.fetchone()
            if not produto:
                print("Produto não encontrado!")
                return

            estoque_atual = produto[0]
            if estoque_atual < qntd_vendida:
                print("Estoque insuficiente!")
                return

            data_venda = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            self.cursor.execute("""
                INSERT INTO vendas(id_cliente, id_produto, qntd_vendida, data_venda)
                VALUES (?, ?, ?, ?)
            """, (id_cliente, id_produto, qntd_vendida, data_venda))

            novo_estoque = estoque_atual - qntd_vendida
            self.cursor.execute("""
                UPDATE produtos SET qntd_estoque = ? WHERE id_produto = ?
            """, (novo_estoque, id_produto))

            self.conexao.commit()
            print(f"Venda registrada com sucesso! ({data_venda})")
        except Exception as e:
            print(f"Erro ao registrar venda: {e}")

    def ver_vendas(self):
        try:
            self.cursor.execute("SELECT * FROM vendas")
            vendas = self.cursor.fetchall()
            if not vendas:
                print("Nenhuma venda registrada!")
                return
            print("\n--- Lista de Vendas ---")
            for venda in vendas:
                id_venda, id_cliente, id_produto, qntd_vendida, data_venda = venda
                print(f"ID: {id_venda} | Cliente: {id_cliente} | Produto: {id_produto} | Qtde: {qntd_vendida} | Data: {data_venda}")
        except Exception as e:
            print(f"Erro ao listar vendas: {e}")

    def deletar_venda(self, id):
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

    def editar_venda(self, id_cliente, id_produto, qntd_vendida, id_venda):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM vendas WHERE id = ?", (id_venda,))
            resultado = self.cursor.fetchone()[0]
            if resultado == 0:
                print("Venda não encontrada!")
                return

            data_venda = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            self.cursor.execute("""
                UPDATE vendas SET id_cliente = ?, id_produto = ?, qntd_vendida = ?, data_venda = ?
                WHERE id = ?
            """, (id_cliente, id_produto, qntd_vendida, data_venda, id_venda))
            self.conexao.commit()
            print(f"Venda editada com sucesso! ({data_venda})")
        except Exception as e:
            print(f"Erro ao editar venda: {e}")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
