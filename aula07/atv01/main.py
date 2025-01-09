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