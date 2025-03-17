from cliente import Clientes
from produto import Produtos
from venda import Vendas

# Instanciar as classes
clientes = Clientes()
produtos = Produtos()
vendas = Vendas()

def menu_clientes():
    while True:
        opcao = input("""
        Menu Clientes:
        1 - Ver clientes
        2 - Adicionar cliente
        3 - Editar cliente
        4 - Deletar cliente
        5 - Voltar
        Digite sua opção: 
        """)
        if opcao == '1':
            clientes.ver_clientes()
        elif opcao == '2':
            nome = input("Nome: ")
            email = input("Email: ")
            endereco = input("Endereço: ")
            clientes.adicionar_cliente(nome, email, endereco)
        elif opcao == '3':
            id = int(input("ID do cliente: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            endereco = input("Novo endereço: ")
            clientes.editar_cliente(nome, email, endereco, id)
        elif opcao == '4':
            id = int(input("ID do cliente: "))
            clientes.deletar_cliente(id)
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
        Digite sua opção: 
        """)
        if opcao == '1':
            produtos.ver_produtos()
        elif opcao == '2':
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            qntd_estoque = int(input("Quantidade em estoque: "))
            preco = float(input("Preço: "))
            produtos.adicionar_produto(nome, descricao, qntd_estoque, preco)
        elif opcao == '3':
            id = int(input("ID do produto: "))
            nome = input("Novo nome: ")
            descricao = input("Nova descrição: ")
            qntd_estoque = int(input("Nova quantidade em estoque: "))
            preco = float(input("Novo preço: "))
            produtos.editar_produto(nome, descricao, qntd_estoque, preco, id)
        elif opcao == '4':
            id = int(input("ID do produto: "))
            produtos.deletar_produto(id)
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
        Digite sua opção: 
        """)
        if opcao == '1':
            vendas.ver_vendas()
        elif opcao == '2':
            id_cliente = int(input("ID do cliente: "))
            id_produto = int(input("ID do produto: "))
            qntd_vendida = int(input("Quantidade vendida: "))
            data_venda = input("Data da venda (AAAA-MM-DD): ")
            vendas.registrar_venda(id_cliente, id_produto, qntd_vendida, data_venda)
        elif opcao == '3':
            id = int(input("ID da venda: "))
            id_cliente = int(input("Novo ID do cliente: "))
            id_produto = int(input("Novo ID do produto: "))
            qntd_vendida = int(input("Nova quantidade vendida: "))
            data_venda = input("Nova data da venda (AAAA-MM-DD): ")
            vendas.editar_venda(id_cliente, id_produto, qntd_vendida, data_venda, id)
        elif opcao == '4':
            id = int(input("ID da venda: "))
            vendas.deletar_venda(id)
        elif opcao == '5':
            break
        else:
            print("Opção inválida!")

# Menu principal
while True:
    opcao = input("""
    Menu Principal:
    1 - Clientes
    2 - Produtos
    3 - Vendas
    * - Sair
    Digite sua opção: 
    """)
    if opcao == '1':
        menu_clientes()
    elif opcao == '2':
        menu_produtos()
    elif opcao == '3':
        menu_vendas()
    elif opcao == '*':
        print("\n----------------------")
        print("Programa encerrado")
        print("----------------------\n")
        break
    else:
        print("Opção inválida!")

# Fechar conexões ao final
clientes.fechar_conexao()
produtos.fechar_conexao()
vendas.fechar_conexao()