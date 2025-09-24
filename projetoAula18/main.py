from cliente import Clientes
from produto import Produtos
from venda import Vendas

clientes = Clientes()
produtos = Produtos()
vendas = Vendas()

def pedir_id_existente(lista_ids, mensagem="ID: "):
    while True:
        try:
            id_digitado = int(input(mensagem))
            if id_digitado in lista_ids:
                return id_digitado
            else:
                print("ID inválido! Digite um ID existente.")
        except ValueError:
            print("Digite um número válido!")

def mostrar_clientes():
    clientes.cursor.execute("SELECT * FROM clientes")
    registros = clientes.cursor.fetchall()
    if not registros:
        print("Nenhum cliente cadastrado!")
        return []
    print("\n--- Lista de Clientes ---")
    for id_cliente, nome, email, endereco in registros:
        print(f"ID: {id_cliente} | Nome: {nome} | Email: {email} | Endereço: {endereco}")
    return [id_cliente for id_cliente, _, _, _ in registros]

def mostrar_produtos():
    produtos.cursor.execute("SELECT * FROM produtos")
    registros = produtos.cursor.fetchall()
    if not registros:
        print("Nenhum produto cadastrado!")
        return []
    print("\n--- Lista de Produtos ---")
    for id_produto, nome, descricao, qntd_estoque, preco in registros:
        print(f"ID: {id_produto} | Nome: {nome} | Desc: {descricao} | Qtde: {qntd_estoque} | Preço: R$ {preco:.2f}")
    return [id_produto for id_produto, _, _, _, _ in registros]

def mostrar_vendas():
    vendas.cursor.execute("SELECT * FROM vendas")
    registros = vendas.cursor.fetchall()
    if not registros:
        print("Nenhuma venda registrada!")
        return []
    print("\n--- Lista de Vendas ---")
    for id_venda, id_cliente, id_produto, qntd_vendida, data_venda in registros:
        print(f"ID: {id_venda} | Cliente: {id_cliente} | Produto: {id_produto} | Qtde: {qntd_vendida} | Data: {data_venda}")
    return [id_venda for id_venda, _, _, _, _ in registros]


def menu_clientes():
    while True:
        opcao = input("""
        Menu Clientes:
        1 - Ver clientes
        2 - Adicionar cliente
        3 - Editar cliente
        4 - Deletar cliente
        5 - Voltar
        
        Digite sua opção: """)
        
        if opcao == '1':
            mostrar_clientes()
        elif opcao == '2':
            nome = input("Nome: ")
            email = input("Email: ")
            endereco = input("Endereço: ")
            clientes.adicionar_cliente(nome, email, endereco)
        elif opcao == '3':
            ids = mostrar_clientes()
            if not ids:
                continue
            print("\n")
            id_cliente = pedir_id_existente(ids, "ID do cliente que deseja editar: ")
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            endereco = input("Novo endereço: ")
            clientes.editar_cliente(nome, email, endereco, id_cliente)
        elif opcao == '4':
            ids = mostrar_clientes()
            if not ids:
                continue
            print("\n")
            id_cliente = pedir_id_existente(ids, "ID do cliente que deseja deletar: ")
            clientes.deletar_cliente(id_cliente)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def menu_produtos():
    while True:
        opcao = input("""
        Menu Produtos:
        1 - Ver produtos
        2 - Adicionar produto
        3 - Editar produto
        4 - Deletar produto
        5 - Voltar
        
        Digite sua opção: """)
        
        if opcao == '1':
            mostrar_produtos()
        elif opcao == '2':
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            qntd_estoque = int(input("Quantidade em estoque: "))
            preco = float(input("Preço: "))
            produtos.adicionar_produto(nome, descricao, qntd_estoque, preco)
        elif opcao == '3':
            ids = mostrar_produtos()
            if not ids:
                continue
            print("\n")
            id_produto = pedir_id_existente(ids, "ID do produto que deseja editar: ")
            nome = input("Novo nome: ")
            descricao = input("Nova descrição: ")
            qntd_estoque = int(input("Nova quantidade em estoque: "))
            preco = float(input("Novo preço: "))
            produtos.editar_produto(nome, descricao, qntd_estoque, preco, id_produto)
        elif opcao == '4':
            ids = mostrar_produtos()
            if not ids:
                continue
            print("\n")
            id_produto = pedir_id_existente(ids, "ID do produto que deseja deletar: ")
            produtos.deletar_produto(id_produto)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def menu_vendas():
    while True:
        opcao = input("""
        Menu Vendas:
        1 - Ver vendas
        2 - Registrar venda
        3 - Editar venda
        4 - Deletar venda
        5 - Voltar
        
        Digite sua opção: """)
        
        if opcao == '1':
            mostrar_vendas()
        elif opcao == '2':
            ids_clientes = mostrar_clientes()
            ids_produtos = mostrar_produtos()
            if not ids_clientes or not ids_produtos:
                print("É necessário ter clientes e produtos cadastrados antes de registrar uma venda!")
                continue
            print("\n")
            id_cliente = pedir_id_existente(ids_clientes, "ID do cliente: ")
            id_produto = pedir_id_existente(ids_produtos, "ID do produto: ")
            qntd_vendida = int(input("Quantidade vendida: "))
            vendas.registrar_venda(id_cliente, id_produto, qntd_vendida)
        elif opcao == '3':
            ids_vendas = mostrar_vendas()
            if not ids_vendas:
                continue
            print("\n")
            id_venda = pedir_id_existente(ids_vendas, "ID da venda que deseja editar: ")
            ids_clientes = mostrar_clientes()
            ids_produtos = mostrar_produtos()
            id_cliente = pedir_id_existente(ids_clientes, "Novo ID do cliente: ")
            id_produto = pedir_id_existente(ids_produtos, "Novo ID do produto: ")
            qntd_vendida = int(input("Nova quantidade vendida: "))
            vendas.editar_venda(id_cliente, id_produto, qntd_vendida, id_venda)
        elif opcao == '4':
            ids_vendas = mostrar_vendas()
            if not ids_vendas:
                continue
            print("\n")
            id_venda = pedir_id_existente(ids_vendas, "ID da venda que deseja deletar: ")
            vendas.deletar_venda(id_venda)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

def main():
    while True:
        opcao = input("""
        Menu Principal:
        1 - Clientes
        2 - Produtos
        3 - Vendas
        * - Sair
        
        Digite sua opção: """)
        
        if opcao == '1':
            menu_clientes()
        elif opcao == '2':
            menu_produtos()
        elif opcao == '3':
            menu_vendas()
        elif opcao == '*':
            print("\n--------------------------")
            print("--- Programa encerrado ---")
            print("--------------------------\n")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
    clientes.fechar_conexao()
    produtos.fechar_conexao()
    vendas.fechar_conexao()
