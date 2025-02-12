from datetime import datetime

class Hotel:
    def __init__(self, nomeHotel):
        self.nomeHotel = nomeHotel
        self.clientes = []
        self.contador_id = 1
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, nome, telefone, email):
        if not nome or not telefone or not email:
            raise ValueError("Nome, telefone e email são obrigatórios.")
        if any(cliente.email == email for cliente in self.clientes):
            raise ValueError("Já existe um cliente com este e-mail.")
        cliente = Cliente(self.contador_id, nome, telefone, email)
        self.clientes.append(cliente)
        self.contador_id += 1
        return cliente

    def listar_clientes(self):
        return self.clientes

    def editar_cliente(self, id, novo_nome, novo_telefone, novo_email):
        cliente = self.obter_cliente_por_id(id)
        if not cliente:
            raise ValueError(f"Cliente com ID {id} não encontrado.")
        cliente.nome = novo_nome
        cliente.telefone = novo_telefone
        cliente.email = novo_email
        return cliente

    def excluir_cliente(self, id):
        cliente = self.obter_cliente_por_id(id)
        if not cliente:
            raise ValueError(f"Cliente com ID {id} não encontrado.")
        self.clientes.remove(cliente)
        return True

    def adicionar_quarto(self, numero, tipo, preco, disponibilidade):
        if any(quarto.numero == numero for quarto in self.quartos):
            raise ValueError(f"Já existe um quarto com o número {numero}.")
        quarto = Quarto(numero, tipo, preco, disponibilidade)
        self.quartos.append(quarto)
        return quarto

    def listar_quartos(self):
        return self.quartos

    def realizar_reserva(self, cliente, quarto, dataEntrada, dataSaida, status):

        if not isinstance(dataEntrada, datetime) or not isinstance(dataSaida, datetime):
            raise ValueError("As datas devem ser do tipo DD/MM/AAAA.")
        
        data_atual = datetime.now()
        
        if dataEntrada < data_atual or dataSaida < data_atual:
            raise ValueError("As datas de Check-In e Check-Out devem ser presentes ou futuras.")
        
        if dataEntrada >= dataSaida:
            raise ValueError("A data de entrada deve ser anterior à data de saída.")
        
        if quarto.disponibilidade != "Disponível":
            raise ValueError("O quarto não está disponível para reserva.")
        
        reserva = Reserva(cliente, quarto, dataEntrada, dataSaida, status)
        self.reservas.append(reserva)
        quarto.disponibilidade = "Ocupado"
        return reserva

    def listar_reservas(self):
        return self.reservas

    def editar_reserva(self, reserva, novo_quarto, nova_dataEntrada, nova_dataSaida, novo_status):
        if reserva not in self.reservas:
            raise ValueError("Reserva não encontrada.")
        if not isinstance(nova_dataEntrada, datetime) or not isinstance(nova_dataSaida, datetime):
            raise ValueError("As datas devem ser do tipo DD/MM/AAAA.")
        
        data_atual = datetime.now()
        
        if nova_dataEntrada < data_atual or nova_dataSaida < data_atual:
            raise ValueError("As datas de Check-In e Check-Out devem ser presentes ou futuras.")
        
        if nova_dataEntrada >= nova_dataSaida:
            raise ValueError("A data de entrada deve ser anterior à data de saída.")
        
        reserva.quarto.disponibilidade = "Disponível"
        
        reserva.quarto = novo_quarto
        reserva.checkIn = nova_dataEntrada
        reserva.checkOut = nova_dataSaida
        reserva.status = novo_status
        
        novo_quarto.disponibilidade = "Ocupado"
        
        return reserva

    def cancelar_reserva(self, reserva):
        if reserva not in self.reservas:
            raise ValueError("Reserva não encontrada.")
        self.reservas.remove(reserva)
        reserva.quarto.disponibilidade = "Disponível"
        return True

    def obter_cliente_por_nome(self, nome):
        return next((cliente for cliente in self.clientes if cliente.nome == nome), None)

    def obter_cliente_por_id(self, id):
        return next((cliente for cliente in self.clientes if cliente.id == id), None)

    def obter_quarto_por_numero(self, numero):
        return next((quarto for quarto in self.quartos if quarto.numero == numero), None)

    def obter_quartos_por_tipo(self, tipo):
        return [quarto for quarto in self.quartos if quarto.tipo == tipo]

    def listar_reservas_por_cliente(self, cliente):
        return [reserva for reserva in self.reservas if reserva.cliente == cliente]

    def listar_reservas_por_quarto(self, quarto):
        return [reserva for reserva in self.reservas if reserva.quarto == quarto]

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
        self._disponibilidade = disponibilidade

    @property
    def disponibilidade(self):
        return self._disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, valor):
        if valor not in ["Disponível", "Ocupado"]:
            raise ValueError("Disponibilidade deve ser 'Disponível' ou 'Ocupado'.")
        self._disponibilidade = valor

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
        return (
            f"Reserva para {self.cliente.nome} - Quarto {self.quarto.numero} - "
            f"Check-In: {self.checkIn.strftime('%d/%m/%Y')} - "
            f"Check-Out: {self.checkOut.strftime('%d/%m/%Y')} - "
            f"Status: {self.status}"
        )


