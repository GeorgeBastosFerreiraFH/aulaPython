class Fatura:
    def __init__(self, nomeItem, preçoUnitario, qntdItens):
        self.nomeItem = nomeItem
        self.preçoUnitario = preçoUnitario
        self.qntdItens = qntdItens

    def gerarFatura(self):
        valorTotal = self.qntdItens * self.preçoUnitario
        return f"Fatura para {self.nomeItem} com valor total de R${valorTotal}"

fatura1 = Fatura(nomeItem="bolsa", preçoUnitario=200, qntdItens=5)

print(fatura1.gerarFatura())


    

