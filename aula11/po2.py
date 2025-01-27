class Celular:
    def __init__(self, modelo, armazenamento, polegadas):
        self.modelo = modelo
        self.armazenamento = armazenamento
        self.statusLigado = False
        self.polegadas = polegadas

    def ligar(self):
        if self.statusLigado:
            print(f"O celular {self.modelo} está ligado.")
        else:
            self.statusLigado = True
            print('O celular esta ligando')

    
celular1 = Celular(modelo="Samsung", armazenamento=128, polegadas=6.1)
celular2 = Celular(modelo="iPhone", armazenamento=256, polegadas=10)
celular3 = Celular(modelo="Xiaomi", armazenamento=512, polegadas=7)

celular1.ligar()
celular1.ligar()

