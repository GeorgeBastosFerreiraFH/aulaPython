import sqlite3

class Produtos:
    def __init__(self, db_file="estoque_loja.db"):
        self.conexao = sqlite3.connect(db_file)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            qntd_estoque INT DEFAULT 0,
            preco DECIMAL(10, 2) NOT NULL
        )
        """)
        self.conexao.commit()

    def adicionar_produto(self, nome, descricao, qntd_estoque, preco):
        try:
            self.cursor.execute("""
            INSERT INTO produtos(nome, descricao, qntd_estoque, preco)
            VALUES (?, ?, ?, ?)
            """, (nome, descricao, qntd_estoque, preco))
            self.conexao.commit()
            print("Produto adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar produto: {e}")

    def ver_produtos(self):
        try:
            self.cursor.execute("SELECT * FROM produtos")
            produtos = self.cursor.fetchall()
            if not produtos:
                print("Nenhum produto cadastrado!")
            else:
                print("\n--- Lista de Produtos ---")
                for id_produto, nome, descricao, qntd_estoque, preco in produtos:
                    print("\n---------------------------")
                    print(f"ID do produto: {id_produto}")
                    print(f"Nome: {nome}")
                    print(f"Descrição: {descricao}")
                    print(f"Quantidade: {qntd_estoque}")
                    print(f"Preço: R$ {preco:.2f}")
                    print("---------------------------")
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")

    def deletar_produto(self, id):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM produtos")
            total = self.cursor.fetchone()[0]
            if total == 0:
                print("Nenhum produto cadastrado!")
                return

            self.cursor.execute("SELECT COUNT(*) FROM produtos WHERE id_produto = ?", (id,))
            resultado = self.cursor.fetchone()[0]
            if resultado == 0:
                print("Produto não encontrado!")
            else:
                self.cursor.execute("DELETE FROM produtos WHERE id_produto = ?", (id,))
                self.conexao.commit()
                print("Produto deletado com sucesso!")
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")

    def editar_produto(self, nome, descricao, qntd_estoque, preco, id):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM produtos WHERE id_produto = ?", (id,))
            resultado = self.cursor.fetchone()[0]
            if resultado == 0:
                print("Produto não encontrado!")
            else:
                self.cursor.execute("""
                UPDATE produtos SET nome = ?, descricao = ?, qntd_estoque = ?, preco = ?
                WHERE id_produto = ?
                """, (nome, descricao, qntd_estoque, preco, id))
                self.conexao.commit()
                print("Produto editado com sucesso!")
        except Exception as e:
            print(f"Erro ao editar produto: {e}")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
