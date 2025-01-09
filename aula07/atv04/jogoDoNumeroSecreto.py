import random

numero_secreto = random.randint(1, 100)

def adivinhar_numeros(numero_secreto):
    for tentativas in range(1, 11):
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
            
            if palpite < 1 or palpite > 100:
                print("\nPor favor, digite um número entre 1 e 100.")
                continue

            if palpite < numero_secreto:
                print("\nO número secreto é maior.")
            elif palpite > numero_secreto:
                print("\nO número secreto é menor.")
            else:
                print(f"\nParabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
                break

            print(f"Você ainda tem {10 - tentativas} tentativas.\n")
        except ValueError:
            print("\nPor favor, digite um número válido.")
    else:
        print(f"\nVocê perdeu! O número secreto era {numero_secreto}.")

adivinhar_numeros(numero_secreto)
