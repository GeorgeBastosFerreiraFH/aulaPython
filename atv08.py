# Atividade 01

listaNumero = [1 , 3, 5, 6, 8, 9, 11, 24, 35, 46, 51, 67, 70, 76, 88, 91, 100, 105, 150]

listaNumerosPares = list(filter(lambda x: x % 2 == 0, listaNumero))

print(listaNumerosPares)

# Atividade 02

produtos = dict()


def adicionarProduto():
    nomeProduto = input('Digite o nome do produto: ')
    precoProduto = float(input('Digite o preço do produto: '))
    qntdEstoque = int(input('Digite a quantidade no estoque: '))

    produtos[nomeProduto] = {
    'Nome': nomeProduto,
    'Preço': precoProduto,
    'Quantidade': qntdEstoque
    }

    print(f'\nProduto {nomeProduto} cadastrado com sucesso!')

def removerProduto():
    if not produtos:
        print('Nenhum produto cadastrado')
    else:
        produtoRemover = int(input('\nDigite a colocação do produto a ser removido: '))

        if 1 <= produtoRemover <= len(produtos):
            produto = list(produtos.keys())
            produto = produto[produtoRemover - 1]
            del produtos[produto]
            print(f'\nProduto {produto} removido com sucesso!')
        else:
            print(f'\nProduto não encontrado.')

def atualizarProduto():
    if not produtos:
        print('Nenhum produto cadastrado')

    else:
        produtoAtualizar = int(input('\nDigite a colocação do produto a ser atualizado: '))

        if 1 <= produtoAtualizar <= len(produtos):
            produto = list(produtos.keys())
            produto = produto[produtoAtualizar - 1]

            while True:
                continuar = input("""
                1 - Nome do produto
                2 - Preço do produto
                3 - Quantidade de estoque do produto
                0 - Sair
                \n""")

                if continuar == '1':
                    nomeNovo = input('Digite o novo nome: ')
                    produtos[produto]['Nome'] = nomeNovo  
                elif continuar == '2':
                    precoNovo = float(input('Digite o novo preço: '))
                    produtos[produto]['Preço'] = precoNovo
                elif continuar == '3':
                    qntdNovo = int(input('Digite a quantidade nova: '))
                    produtos[produto]['Quantidade'] = qntdNovo
                elif continuar == '0':
                    print("Programa encerrado!")
                    break
                else:
                    print('Opção inválida.')


            print(f'\nProduto {produto} atualizado com sucesso!')
        else:
            print(f'\nProduto não encontrado.') 

def verProdutos():
    if not produtos:
        print('Nenhum produto cadastrado')
    else:
        for contador,(nome , dados) in enumerate(produtos.items(), start=1):
            print('\n----------------------')
            print(f'{contador}º produto')
            print('----------------------')
            print(f'{dados['Nome']}')
            print(f'R$ {dados['Preço']}')
            print(f'Quantidade em estoque {dados['Quantidade']}')
            print('----------------------')

while True:
    continuar = input("""
    1 - Cadastrar produto
    2 - Remover produto
    3 - Atualizar produto
    4 - Ver produtos cadastrados
    0 - Sair
    \n""")
    if continuar == '1':
        adicionarProduto()
    
    elif continuar == '2':
        removerProduto()
    elif continuar == '3':
        atualizarProduto()
    elif continuar == '4':
        verProdutos()

    elif continuar == '0':
        print("Programa encerrado!")
        break
    else:
        print('Opção inválida.')

# Atividade 03

listaCores = ['azul', 'amarelo', 'verde', 'vermelho','rosa', 'branco', 'preto']

def contarLetras():
    for letras in listaCores:
        qntdLetras = len(letras)

        if qntdLetras >= 4:
            print(letras)
    
contarLetras()

# Atividade 04

lista = dict()

def listaPalavras():
    while True:
        palavra = input('Digite uma palavra ou 0 para sair: ')

        if palavra == '0':
            break

        lista[palavra] = palavra


def listaPalindromo():
    for palavra in lista:
        if palavra == palavra[::-1]:
            lista[palavra] = "Palíndromo"
        else:
            lista[palavra] = "Não é palíndromo"

listaPalavras()
listaPalindromo()

print('-------------------------')
print("Palíndromos encontrados:")
print('-------------------------')
for palavra, status in lista.items():
    if status == "Palíndromo":
        print(palavra)
print('-------------------------')

# Atividade 05 - Utilizando IA

vendas = {
    'produto1': 150,
    'produto2': 300,
    'produto3': 300,
    'produto4': 200
}

max_vendas = max(vendas.values())
produtos_mais_vendidos = [produto for produto, vendas in vendas.items() if vendas == max_vendas]

print("Produto(s) mais vendido(s):", ', '.join(produtos_mais_vendidos))


# Atividade 06 - Utilizando IA

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

count_impares = sum(1 for numero in numeros if numero % 2 != 0)

count_pares = sum(1 for numero in numeros if numero % 2 == 0)

print("Quantidade de números ímpares:", count_impares)
print("Quantidade de números pares:", count_pares)


# Atividade 07 - Utilizando IA

vendas_trimestrais = [
    [1000, 1200, 1100],  # Janeiro a Março
    [1500, 1400, 1600],  # Abril a Junho
    [1700, 1800, 1600],  # Julho a Setembro
    [1900, 2000, 2100]   # Outubro a Dezembro
]

medias_trimestrais = [sum(trimestre) / len(trimestre) for trimestre in vendas_trimestrais]

for i, media in enumerate(medias_trimestrais):
    print(f"Média de vendas do Trimestre {i+1}: {media:.2f}")

# Atividade 07/2 - Utilizando IA

max_vendas = max(vendas_trimestrais, key=sum)
trimestre_mais_vendas = vendas_trimestrais.index(max_vendas) + 1

min_vendas = min(vendas_trimestrais, key=sum)
trimestre_menos_vendas = vendas_trimestrais.index(min_vendas) + 1

total_vendas_ano = sum(sum(trimestre) for trimestre in vendas_trimestrais)


print(f"Trimestre com a maior soma de vendas: Trimestre {trimestre_mais_vendas}")
print(f"Trimestre com a menor soma de vendas: Trimestre {trimestre_menos_vendas}")
print(f"Total de vendas no ano inteiro: {total_vendas_ano}")
