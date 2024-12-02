# # Atividade 01

calculadora.py

def somar(num1, num2):
  return f'O resultado da soma é {num1 + num2}\n'

def subtrair(num1, num2):
  return f'O resultado da subtração é {num1 - num2}\n'

def multiplicar(num1, num2):
  return f'O resultado da multiplicação é {num1 * num2}\n'

def dividir(num1, num2):
  return f'O resultado da divisão é {num1 / num2}\n'


main.py

import calculadora

while True:

  numero1 = int(input('Digite o primeiro número: '))
  numero2 = int(input('Digite o segundo número: ')) 

  continuar = input("""
  1 - Somar
  2 - Subtrair
  3 - Dividir
  4 - Multiplicar
  * - Sair
  """)
  if continuar == '1':
    soma = calculadora.somar(numero1, numero2)
    print(soma)
  elif continuar == '2':
    subtracao = calculadora.subtrair(numero1, numero2)
    print(subtracao)
  elif continuar == '3':
    divisao = calculadora.dividir(numero1, numero2)
    print(divisao)
  elif continuar == '4':
    multiplicacao = calculadora.multiplicar(numero1, numero2)
    print(multiplicacao)
  elif continuar == '*':
    print("Programa encerrado!")
    break
  else:
    print('Opção inválida. Digite S para sair ou alguma função válida')



# # Atividade 02
