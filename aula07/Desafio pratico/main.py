livros = dict()
emprestimos = dict()

def adicionar_livros():
    titulo = input('Digite o título do livro: ')
    autor = input('Digite o autor do livro: ')
    qntd_copias = input('Digite quantas cópias do livro: ')

    livros[titulo] = {
        'autor': autor,
        'qntd_copias': int(qntd_copias),
        'alugado': 0
    }
    print('\nLivro adicionado com sucesso!')

def listar_livros():
    if not livros:
        print('Nenhum livro cadastrado.')
        return

    print('----------------------')
    print('Lista de livros')
    print('----------------------\n')
    for contador, (nome, info) in enumerate(livros.items(), start=1):
        disponivel = "Sim" if info["qntd_copias"] > info["alugado"] else "Não"
        print(f'{contador}º livro')
        print('----------------------')
        print(f'Título: {nome}') 
        print(f'Autor: {info["autor"]}') 
        print(f'Quantidade de cópias: {info["qntd_copias"]}')
        print(f'Quantas cópias estão emprestadas: {info["alugado"]}')
        print(f'Disponível: {disponivel}')
        print('----------------------\n')

def buscar_livro():
    if not livros:
        print('Nenhum livro cadastrado.')

    titulo = input('Digite o título do livro: ')
    if titulo in livros:
        disponivel = "Sim" if livros[titulo]["qntd_copias"] > livros[titulo]["alugado"] else "Não"
        print(f'\nTítulo: {titulo}')
        print(f'Autor: {livros[titulo]["autor"]}')
        print(f'Quantidade de cópias: {livros[titulo]["qntd_copias"]}')
        print(f'Quantas cópias estão emprestadas: {livros[titulo]["alugado"]}')
        print(f'Disponível: {disponivel}')
    else:
        print('Livro não encontrado.')

def alugar_livro():
    if not livros:
        print('Nenhum livro cadastrado.')
        return

    titulo = input('Digite o título do livro: ')
    
    if titulo not in livros:
        print('Livro não encontrado.')
        return

    if livros[titulo]["qntd_copias"] - livros[titulo]["alugado"] <= 0:
        print('Não há cópias disponíveis para alugar.')
        return

    usuario = input('Digite seu nome para alugar o livro: ')
    if usuario not in emprestimos:
        emprestimos[usuario] = []

    emprestimos[usuario].append(titulo)
    livros[titulo]["alugado"] += 1
    print(f'Livro "{titulo}" alugado com sucesso para {usuario}.')

def devolver_livro():
    if not livros:
        print('Nenhum livro cadastrado.')
        return

    usuario = input('Digite seu nome para devolver o livro: ')
    if usuario not in emprestimos or not emprestimos[usuario]:
        print(f'{usuario} não tem livros emprestados.')
        return

    titulo = input('Digite o título do livro a ser devolvido: ')
    if titulo not in emprestimos[usuario]:
        print(f'{usuario} não tem esse livro emprestado.')
        return

    emprestimos[usuario].remove(titulo)
    livros[titulo]["alugado"] -= 1
    livros[titulo]["qntd_copias"] += 1
    print(f'Livro "{titulo}" devolvido com sucesso.')

def verificar_disponibilidade():
    if not livros:
        print('Nenhum livro cadastrado.')
        return

    titulo = input('Digite o título do livro para verificar a disponibilidade: ').lower()
    if titulo not in livros:
        print('Livro não encontrado.')
        return

    disponivel = livros[titulo]["qntd_copias"] - livros[titulo]["alugado"]
    if disponivel > 0:
        print(f'O livro "{titulo}" está disponível para empréstimo.')
    else:
        print(f'O livro "{titulo}" não está disponível para empréstimo no momento.')

def listar_emprestimos_usuario():
    if not emprestimos:
        print('Nenhum empréstimo realizado.')
        return

    usuario = input('Digite seu nome para ver seus empréstimos: ')
    if usuario not in emprestimos or not emprestimos[usuario]:
        print(f'{usuario} não tem livros emprestados.')
        return

    print(f'Livros emprestados para {usuario}:')
    for livro in emprestimos[usuario]:
        print(f'- {livro}')

def exibir_menu():
    print("""
    -------------------------
    1 - Adicionar livro
    2 - Listar livros
    3 - Buscar livro
    4 - Alugar livro
    5 - Devolver livro
    6 - Verificar disponibilidade de livro
    7 - Listar empréstimos de um usuário
    0 - Sair
    -------------------------
    """)

def main():
    while True:
        exibir_menu()
        opcao = input('Digite a opção desejada: ')

        if opcao == '0':
            print('\n----------------------')
            print('Programa encerrado')
            print('----------------------\n')
            break

        if opcao == '1':
            adicionar_livros()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            alugar_livro()
        elif opcao == '5':
            devolver_livro()
        elif opcao == '6':
            verificar_disponibilidade()
        elif opcao == '7':
            listar_emprestimos_usuario()
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()
