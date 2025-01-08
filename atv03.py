# Atividade 1

idade = int(input('Digite sua idade: '))

if idade < 12 and  idade > 0:
  print('Você é criança')
elif idade >= 12 and idade <= 17:
  print('Você é adolescente')
elif idade >= 18 and idade <= 59:
  print('Você é adulto')
elif idade >= 60:
  print('Você é idoso')
else:
  print('Idade inválida')

print('------------------------------------')

# Atividade 2

numeros = set()

for numero in range(3):
  numeros.add(int(input('Digite um número: ')))

maiorNumero = float('-inf')
menorNumero = float('inf')

for numero in numeros:
  if numero > maiorNumero:
    maiorNumero = numero

print(f'Esse é o maior número digitado: {maiorNumero}')

for numero in numeros:
  if numero < menorNumero:
    menorNumero = numero

print(f'Esse é o menor número digitado: {menorNumero}')

print(numeros)

print('------------------------------------')

# Atividade 3

numeros = set()

print('Digite 10 números inteiros')
for numero in range(10):
  numeros.add(int(input('Digite um número: ')))

numerosPar = set()
numerosImpar = set()

for numero in numeros:
  if numero % 2 == 0:
    numerosPar.add(numero)
  else:
    numerosImpar.add(numero)

print(f'Esses são os números pares: {numerosPar}')
print(f'Esses são os números impares: {numerosImpar}')

# Atividade 4

pessoas = dict()

def cadastrar_pessoas():  
  nome = input('Digite o nome da pessoa: ')
  idade = int(input('Digite a idade da pessoa: '))
  pessoas[nome] = idade
  print(f'\nPessoa {nome} cadastrada com sucesso!\n')

def calcular_media_idade():
  if not pessoas:
    print('Nenhuma pessoa cadastrada.')
    return

  soma = 0
  for pessoa in pessoas:
    soma += pessoas[pessoa]
  media = soma / len(pessoas)
  if media >= 0 and media <= 25:
    print('A média da turma é de jovens')
  elif media > 25 and media < 60:
    print('A média da turma é de adultos')
  elif media >= 60:
    print('A média da turma é de idosos')
  
  print(f'A média de idade é {media:.2f}')

while True:
  continuar = input("""
  1 - Cadastrar pessoas
  2 - Calcular média de idade
  0 - Sair

  """)
  if continuar == '1':
    cadastrar_pessoas()

  elif continuar == '2':
    calcular_media_idade()

  elif continuar == '0':
    print("Programa encerrado!")
    break
  else:
    print('Opção inválida.')

# Atividade 5

numeros = {}

def digitar_numeros():
    qntd_numeros = int(input('\nQuantos números deseja digitar? '))
    
    for contador in range(qntd_numeros):
        numero = int(input(f'Digite o número {contador + 1}: '))
        numeros[f"Número {contador + 1}"] = numero
    
    print(f'\nNúmeros cadastrados: {numeros}')

def determinar_menor_valor():
    if not numeros:
        print('\nNenhum número cadastrado.')
        return
    menor_valor = min(numeros.values())
    print(f'\nO menor valor é {menor_valor}')

def determinar_maior_valor():
    if not numeros:
        print('\nNenhum número cadastrado.')
        return
    maior_valor = max(numeros.values())
    print(f'\nO maior valor é {maior_valor}')

def determinar_soma_valor():
    if not numeros:
        print('\nNenhum número cadastrado.')
        return
    soma_valores = sum(numeros.values())
    print(f'\nA soma dos valores é {soma_valores}')

while True:
    continuar = input("""
    1 - Digitar números
    2 - Determinar menor valor
    3 - Determinar maior valor
    4 - Determinar soma dos valores
    0 - Sair
    \n""")
    
    if continuar == '1':
        digitar_numeros()
    elif continuar == '2':
        determinar_menor_valor()
    elif continuar == '3':
        determinar_maior_valor()
    elif continuar == '4':
        determinar_soma_valor()
    elif continuar == '0':
        print('\n-------------------')
        print('Programa encerrado!')
        print('-------------------\n')
        break
    else:
        print('Opção inválida.')

#  Desafio Pratico

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
    if not produtos:
        print('Nenhum produto cadastrado.')
        return
    produtos_mil = dict()
    for produto in produtos:
        if produtos[produto] > 1000:
            produtos_mil[produto] = produtos[produto]
        elif produtos[produto] < 1000:
            print('Nenhum produto acima de R$1000')
            return
    print(f'O produto que custa mais de R$1000 é: {produtos_mil}')

def menor_valor():
    menor = float("inf")
    nome_produto = ""
    for produto, preco in produtos.items():
        if preco < menor:
            menor = preco
            nome_produto = produto
      
    print(f"O produto com menor preço é '{nome_produto}' custando R${menor:.2f}")

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
    print('Opção inválida.')

