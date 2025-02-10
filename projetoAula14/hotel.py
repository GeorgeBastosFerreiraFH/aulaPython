class Hotel:
    def __init__(self, nomeHotel):
        self.nomeHotel = nomeHotel
        self.clientes = []
        self.contador_id = 1
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, nome, telefone, email):
        cliente = Cliente(self.contador_id, nome, telefone, email)
        self.clientes.append(cliente)
        self.contador_id += 1

    def listar_cliente(self):
        if not self.clientes:
            return "Não há clientes nesse hotel."
        
        return "\n".join(str(cliente) for cliente in self.clientes)
    
def editar_cliente(self, id, novo_nome, novo_telefone, novo_email):
    if not self.clientes:
        return "Não há clientes nesse hotel."

    for cliente in self.clientes:
        if cliente.id == id:
            cliente.nome = novo_nome
            cliente.telefone = novo_telefone
            cliente.email = novo_email
            return f"Cliente {novo_nome} atualizado com sucesso"
    
    return f"Cliente com ID {id} não encontrado."


class Cliente:
    def __init__(self, id, nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"ID: {self.id} - Cliente: {self.nome} - Telefone: {self.telefone} - Email: {self.email}"

class Quarto:
    def __init__(self, numero, tipo, preco, disponibilidade):
        self.numero = numero
        self.tipo = tipo
        self.preco = preco
        self.disponibilidade = disponibilidade

    def __str__(self):
        return f"Número do quarto: {self.numero} - Tipo de quarto: {self.tipo} - Preço da diária: {self.preco} - Status: {self.disponibilidade}"

class Reserva:
    def __init__(self, cliente, quarto, dataEntrada, dataSaida, status):
        self.cliente = cliente
        self.quarto = quarto
        self.checkIn = dataEntrada
        self.checkOut = dataSaida
        self.status = status
    
    def __str__(self):
        return f"Dono do quarto {self.cliente} - Quarto reservado {self.quarto} - Check-In {self.checkIn} / Check-out {self.checkOut} - Reserva {self.status}"
    