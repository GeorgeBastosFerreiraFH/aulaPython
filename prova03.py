produtos = dict()

def cadastrar_produto():
  nomeProduto = input('Digite o nome do produto: ')
  precoProduto = float(input('Digite o preço do produto: '))

  produtos[nomeProduto] = precoProduto
  print(f'\nProduto {nomeProduto} cadastrado com sucesso!\n')

def total_gasto():
  total = 0
  for produto in produtos:
    total += produtos[produto]
  print(f'O total gasto foi de R${total:.2f}')

while True:
  continuar = input("""
  1 - Cadastrar produto
  2 - Ver total gasto
  0 - Sair

  """)
  if continuar == '1':
    cadastrar_produto()
  elif continuar == '2':
    total_gasto()
  elif continuar == '0':
    print("Programa encerrado!")
    break
  else:
    print('Opção inválida. Por favor, digite 1 para sair ou 2 para continuar')
