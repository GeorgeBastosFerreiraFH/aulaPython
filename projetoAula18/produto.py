import sqlite3

class Produtos:
    def __init__(self, db_file="estoque_loja.db"):
        self.conexao = sqlite3.connect(db_file)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        """Cria a tabela 'produtos' se ela ainda não existir."""
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
        """Adiciona um novo produto à tabela 'produtos'."""
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
        """Exibe todos os produtos cadastrados na tabela 'produtos'."""
        try:
            self.cursor.execute("SELECT * FROM produtos")
            produtos = self.cursor.fetchall()

            if not produtos:
                print("Nenhum produto cadastrado")
            else:
                for produto in produtos:
                    print(produto)
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")

    def deletar_produto(self, id):
        """Deleta um produto da tabela 'produtos' pelo ID."""
        try:
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
        """Edita os dados de um produto na tabela 'produtos' pelo ID."""
        try:
            self.cursor.execute("SELECT COUNT(*) FROM produtos WHERE id_produto = ?", (id,))
            resultado = self.cursor.fetchone()[0]
            if resultado == 0:
                print("Produto não encontrado!")
            else:
                self.cursor.execute("""
                UPDATE produtos SET nome = ?, descricao = ?, qntd_estoque = ?, preco = ? WHERE id_produto = ?
                """, (nome, descricao, qntd_estoque, preco, id))
                self.conexao.commit()
                print("Produto editado com sucesso!")
        except Exception as e:
            print(f"Erro ao editar produto: {e}")

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        self.cursor.close()
        self.conexao.close()