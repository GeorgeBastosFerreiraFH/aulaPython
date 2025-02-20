class ContaBancaria:
    def __init__(self, nome_cliente, saldo=0):
        self._nome_cliente = nome_cliente
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
            else:
                print("Saldo insuficiente para saque.")

    def exibir_saldo(self):
        print(f"Saldo do Cliente {self._nome_cliente}: R${self._saldo:.2f}")

conta = ContaBancaria("Fulano", 1000)
conta.depositar(500)
conta.sacar(200)
conta.sacar(2000)
conta.exibir_saldo()
