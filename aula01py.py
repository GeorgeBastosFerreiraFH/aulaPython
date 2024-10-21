numero_procurado = 7

for i in range(1, 11):
  if i == numero_procurado:
    print(f'Número {numero_procurado} encontrado')
  print(i)

print('------------------------------------')

for i in range(1, 11):
  if i % 2 != 0:
    continue
  print(i)

print('------------------------------------')

for num in range(2 , 20):
  for i in range(2, num):
    if num % i == 0:
      break
  else:
    print(f'{num} é um número primo!')
   
print('------------------------------------')

listaDeNumeros = [1, 2, 3, 4, 5]
listaDeLetras = ['a', 'e', 'i', 'o', 'u']
# listaDeLogicos = [True, False, False, True]
listaMista = ['Gabriel', 9, '3º Elemento', True, 8.9]

# Atividade 1

print('Elementos da lista de números: ')
for i in listaDeNumeros:
  print(i)

print('------------------------------------')
# Atividade 2

print('Elementos da lista de letras: ')
for i in listaDeLetras:
  print(i)

print('------------------------------------')
# Atividade 3

print(listaMista[2])


print('------------------------------------')

# *****************************************
for indice, vogal in enumerate(listaDeLetras, start=1):
    print(f'vogal {indice}: {vogal}')
# *****************************************

print('------------------------------------')

lista_compras = [
  '10 pcts. de arroz', 
  '3 pcts. feijão', 
  '5 kgs carne', 
  '2 caixas ovos', 
  '2 caixas leite'
  ]

print('LISTA DE COMPRAS', end='\n\n')
for indice, item in enumerate(lista_compras, start=1):
  print(f"Produto {indice}:  [  ] {item}" )

