from conversao import *

def menu_principal():
    print("""
        Escolha uma categoria:
        1 - Medidas de Comprimento
        2 - Medidas de Massa
        3 - Temperatura
        0 - Sair
        """)

def menu_comprimento():
    print("""
        Escolha uma conversão:
        1 - Metros para Pés
        2 - Pés para Metros
        3 - Quilômetros para Milhas
        4 - Milhas para Quilômetros
        0 - Voltar
        """)

def menu_massa():
    print("""
        Escolha uma conversão:
        1 - Quilogramas para Libras
        2 - Libras para Quilogramas
        3 - Gramas para Onças
        4 - Onças para Gramas
        0 - Voltar
        """)

def menu_temperatura():
    print("""
        Escolha uma conversão:
        1 - Celsius para Fahrenheit
        2 - Fahrenheit para Celsius
        3 - Celsius para Kelvin
        4 - Kelvin para Celsius
        0 - Voltar
        """)

def main():
    while True:
        menu_principal()
        escolha = int(input("Digite sua escolha: "))

        if escolha == 0:
            print("Encerrando o programa.")
            break

        elif escolha == 1:  
            while True:
                menu_comprimento()
                opcao = int(input("Escolha uma opção: "))
                if opcao == 0:
                    break

                valor = float(input("Digite o valor para conversão: "))

                if opcao == 1:
                    print(f"{valor} metros equivalem a {metros_para_pes(valor):.2f} pés.")
                elif opcao == 2:
                    print(f"{valor} pés equivalem a {pes_para_metros(valor):.2f} metros.")
                elif opcao == 3:
                    print(f"{valor} quilômetros equivalem a {quilometros_para_milhas(valor):.2f} milhas.")
                elif opcao == 4:
                    print(f"{valor} milhas equivalem a {milhas_para_quilometros(valor):.2f} quilômetros.")
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha == 2:         
            while True:
                menu_massa()
                opcao = int(input("Escolha uma opção: "))
                if opcao == 0:
                    break

                valor = float(input("Digite o valor para conversão: "))

                if opcao == 1:
                    print(f"{valor} quilogramas equivalem a {quilogramas_para_libras(valor):.2f} libras.")
                elif opcao == 2:
                    print(f"{valor} libras equivalem a {libras_para_quilogramas(valor):.2f} quilogramas.")
                elif opcao == 3:
                    print(f"{valor} gramas equivalem a {gramas_para_oncas(valor):.2f} onças.")
                elif opcao == 4:
                    print(f"{valor} onças equivalem a {oncas_para_gramas(valor):.2f} gramas.")
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha == 3:  
            while True:
                menu_temperatura()
                opcao = int(input("Escolha uma opção: "))
                if opcao == 0:
                    break

                valor = float(input("Digite o valor para conversão: "))

                if opcao == 1:
                    print(f"{valor} °C equivalem a {celsius_para_fahrenheit(valor):.2f} °F.")
                elif opcao == 2:
                    print(f"{valor} °F equivalem a {fahrenheit_para_celsius(valor):.2f} °C.")
                elif opcao == 3:
                    print(f"{valor} °C equivalem a {celsius_para_kelvin(valor):.2f} K.")
                elif opcao == 4:
                    print(f"{valor} K equivalem a {kelvin_para_celsius(valor):.2f} °C.")
                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
