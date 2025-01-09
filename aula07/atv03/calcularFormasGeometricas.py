import math

def calcularAreaQuadrado(lado):
    area = lado ** 2
    print("A área do quadrado é:", area)

def calcularPerimetroQuadrado(lado):
    perimetro = 4 * lado
    print("O perímetro do quadrado é:", perimetro)

def calcularAreaRetangulo(base, altura):
    area = base * altura
    print("A área do retângulo é:", area)

def calcularPerimetroRetangulo(base, altura):
    perimetro = 2 * (base + altura)
    print("O perímetro do retângulo é:", perimetro)

def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    print("A área do triângulo é:", area)

def calcularPerimetroTriangulo(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3
    print("O perímetro do triângulo é:", perimetro)

def calcularAreaCirculo(raio):
    area = math.pi * (raio ** 2)
    print(f"A área do círculo é: {area:.2f}")

def calcularPerimetroCirculo(raio):
    perimetro = 2 * math.pi * raio
    print(f"O perímetro do círculo é: {perimetro:.2f}")

def exibir_menu():
    print("""
    -------------------------
    1 - Calcular Area Quadrado
    2 - Calcular Perimetro Quadrado
    3 - Calcular Area Retângulo
    4 - Calcular Perimetro Retângulo
    5 - Calcular Area Triângulo
    6 - Calcular Perimetro Triângulo
    7 - Calcular Area Círculo
    8 - Calcular Perimetro Círculo
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
            calcularAreaQuadrado(float(input("Digite o lado do quadrado: ")))
        elif opcao == '2':
            calcularPerimetroQuadrado(float(input("Digite o lado do quadrado: ")))
        elif opcao == '3':
            calcularAreaRetangulo(float(input("Digite a base do retângulo: ")), float(input("Digite a altura do retângulo: ")))
        elif opcao == '4':
            calcularPerimetroRetangulo(float(input("Digite a base do retângulo: ")), float(input("Digite a altura do retângulo: ")))
        elif opcao == '5':
            calcularAreaTriangulo(float(input("Digite a base do triângulo: ")), float(input("Digite a altura do triângulo: ")))
        elif opcao == '6':
            calcularPerimetroTriangulo(float(input("Digite o lado 1 do triângulo: ")), float(input("Digite o lado 2 do triângulo: ")), float(input("Digite o lado 3 do triângulo: ")))
        elif opcao == '7':
            calcularAreaCirculo(float(input("Digite o raio do círculo: ")))
        elif opcao == '8':
            calcularPerimetroCirculo(float(input("Digite o raio do círculo: ")))
        
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()
