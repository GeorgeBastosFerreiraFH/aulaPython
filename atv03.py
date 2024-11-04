# # Atividade 1

# idade = int(input('Digite sua idade: '))

# if idade < 12 and  idade > 0:
#   print('Você é criança')
# elif idade >= 12 and idade <= 17:
#   print('Você é adolescente')
# elif idade >= 18 and idade <= 59:
#   print('Você é adulto')
# elif idade >= 60:
#   print('Você é idoso')
# else:
#   print('Idade inválida')

# print('------------------------------------')
# # Atividade 2

# numeros = set()

# for numero in range(3):
#   numeros.add(int(input('Digite um número: ')))

# comparar = 0

# for numero in numeros:
#   if numero > comparar:
#     maiorNumero = numero

# print(f'Esse é o maior número digitado: {maiorNumero}')

# for numero in numeros:
#   if numero < comparar:
#     menorNumero = numero

# print(f'Esse é o menor número digitado: {menorNumero}')

# print(numeros)

# # print('------------------------------------')

# #  Desafio Pratico

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

def produtos_maior_mil():
  produtos_mil = dict()
  for produto in produtos:
    if produtos[produto] > 1000:
      produtos_mil[produto] = produtos[produto]
  print(f'O produto que custa mais de R$1000 é: {produtos_mil}')

def menor_valor():
  menor = float("inf")
  nome_produto = ""
  for produto, preco in produtos.items():  # Itera diretamente sobre chave-valor
    if preco < menor:
      menor = preco
      nome_produto = produto

while True:
  continuar = input("""
  1 - Cadastrar produto
  2 - Ver total gasto
  3 - Ver produtos acima de R$1000
  4 - Ver nome do produto com menor preço
  0 - Sair

  """)
  if continuar == '1':
    cadastrar_produto()
    
  elif continuar == '2':
    total_gasto()
  elif continuar == '3':
    produtos_maior_mil()
  elif continuar == '4':
    menor_valor()

  elif continuar == '0':
    print("Programa encerrado!")
    break
  else:
    print('Opção inválida. Por favor, digite 1 para sair ou 2 para continuar')
    


