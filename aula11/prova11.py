class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som
        
    def emitir_som(self):
        return f"{self.nome} faz {self.som}!"
    
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Au Au Auuuuuuu")
        
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "miaaauuuuuu")

gato = Gato("Bola de Neve")
cachorro = Cachorro("Duque")

print(gato.emitir_som())
print(cachorro.emitir_som())
