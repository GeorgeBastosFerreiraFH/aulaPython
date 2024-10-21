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
listaDeLogicos = [True, False, False, True]
listaMista = ['Gabriel', 9, '3º Elemento', True, 'Maria']

# Atividade 1

for i in listaDeNumeros:
  print(i)

print('------------------------------------')
# Atividade 2

for i in listaDeLetras:
  print(i)

print('------------------------------------')
# Atividade 3

print(listaMista[2])

print('------------------------------------')
# Atividade 4
