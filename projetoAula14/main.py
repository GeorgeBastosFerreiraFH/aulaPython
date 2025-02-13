import flet as ft
from hotel import Hotel
from datetime import datetime, timedelta

# Cria uma instância do hotel
hotel = Hotel("Estadia dos Sonhos")

# Adiciona alguns quartos para teste
hotel.adicionar_quarto(101, "Single", 100.0, "Disponível")
hotel.adicionar_quarto(102, "Double", 150.0, "Disponível")
hotel.adicionar_quarto(103, "Suite", 200.0, "Disponível")
hotel.adicionar_quarto(104, "Single", 100.0, "Disponível")
hotel.adicionar_quarto(105, "Double", 150.0, "Disponível")
hotel.adicionar_quarto(106, "Suite", 200.0, "Disponível")
hotel.adicionar_quarto(107, "Single", 100.0, "Disponível")
hotel.adicionar_quarto(108, "Double", 150.0, "Disponível")

# Adiciona alguns clientes para teste
hotel.adicionar_cliente("Carlos Souza", "9999-8888", "carlos@email.com")
hotel.adicionar_cliente("Ana Paula", "7777-6666", "ana@email.com")
hotel.adicionar_cliente("Fernando Lima", "5555-4444", "fernando@email.com")
hotel.adicionar_cliente("João Silva", "1234-5678", "joao@email.com")
hotel.adicionar_cliente("Maria Oliveira", "8765-4321", "maria@email.com")
hotel.adicionar_cliente("Pedro Santos", "1111-2222", "pedro@email.com")
hotel.adicionar_cliente("Juliana Costa", "3333-4444", "juliana@email.com")
hotel.adicionar_cliente("Lucas Pereira", "5555-6666", "lucas@email.com")

# Adicionando reservas de teste
cliente1 = hotel.obter_cliente_por_nome("Carlos Souza")
quarto1 = hotel.obter_quarto_por_numero(101)
data_entrada1 = datetime.now() + timedelta(days=1)
data_saida1 = datetime.now() + timedelta(days=5)
hotel.realizar_reserva(cliente1, quarto1, data_entrada1, data_saida1, "Confirmada")

cliente2 = hotel.obter_cliente_por_nome("Ana Paula")
quarto2 = hotel.obter_quarto_por_numero(102)
data_entrada2 = datetime.now() + timedelta(days=2)
data_saida2 = datetime.now() + timedelta(days=6)
hotel.realizar_reserva(cliente2, quarto2, data_entrada2, data_saida2, "Confirmada")

cliente3 = hotel.obter_cliente_por_nome("Fernando Lima")
quarto3 = hotel.obter_quarto_por_numero(103)
data_entrada3 = datetime.now() + timedelta(days=3)
data_saida3 = datetime.now() + timedelta(days=7)
hotel.realizar_reserva(cliente3, quarto3, data_entrada3, data_saida3, "Pendente")

# Definição de cores
COR_PRIMARIA = "#1565C0"  # Azul escuro
COR_SECUNDARIA = "#90CAF9"  # Azul claro
COR_FUNDO = "#F5F5F5"  # Cinza claro
COR_TEXTO = "#212121"  # Quase preto
COR_DESTAQUE = "#4CAF50"  # Verde
COR_ALERTA = "#F44336"  # Vermelho

def main(page: ft.Page):
    page.title = "Sistema de Gerenciamento do Hotel"
    page.theme_mode = "light"
    page.bgcolor = COR_FUNDO
    page.padding = 0
    page.spacing = 0
    page.window_width = 1000
    page.window_height = 800
    page.window_resizable = False

    def estilo_card():
        return {
            "border": ft.border.all(1, COR_SECUNDARIA),
            "border_radius": 10,
            "padding": 20,
            "bgcolor": "white",
        }

    def estilo_botao(cor_fundo=COR_PRIMARIA, cor_texto="white"):
        return ft.ButtonStyle(
            color=cor_texto,
            bgcolor=cor_fundo,
            padding=10,
            shape=ft.RoundedRectangleBorder(radius=8),
        )

    def exibir_mensagem(mensagem, cor=COR_ALERTA):
        page.snack_bar = ft.SnackBar(ft.Text(mensagem, color="white"), bgcolor=cor)
        page.snack_bar.open = True
        page.update()

    def atualizar_conteudo_dinamico(conteudo):
        conteudo_dinamico.content.controls.clear()
        conteudo_dinamico.content.controls.append(conteudo)
        page.update()

    # Função para exibir a lista de quartos
    def exibir_quartos(e):
        lista_quartos = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=300,
            spacing=20,
            run_spacing=20,
        )
        for quarto in hotel.listar_quartos():
            lista_quartos.controls.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(f"Quarto {quarto.numero}", size=18, weight="bold", color=COR_PRIMARIA),
                            ft.Text(f"Tipo: {quarto.tipo}", color=COR_TEXTO),
                            ft.Text(f"Preço: R${quarto.preco:.2f}", color=COR_TEXTO),
                            ft.Text(
                                f"Status: {quarto.disponibilidade}",
                                color=COR_DESTAQUE if quarto.disponibilidade == "Disponível" else COR_ALERTA
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    **estilo_card(),
                )
            )

        atualizar_conteudo_dinamico(
            ft.Column(
                [
                    ft.Text("Quartos Disponíveis", size=24, weight="bold", color=COR_PRIMARIA),
                    lista_quartos,
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    # Função para exibir a lista de clientes
    def exibir_clientes(e):
        lista_clientes = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=300,
            spacing=20,
            run_spacing=20,
        )
        if hotel.listar_clientes():
            for cliente in hotel.listar_clientes():
                lista_clientes.controls.append(
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(cliente.get_nome(), size=18, weight="bold", color=COR_PRIMARIA),
                                ft.Text(f"Telefone: {cliente.get_telefone()}", color=COR_TEXTO),
                                ft.Text(f"Email: {cliente.get_email()}", color=COR_TEXTO),
                                ft.Row(
                                    [
                                        ft.ElevatedButton("Editar", on_click=lambda e, c=cliente: exibir_editar_cliente(c), style=estilo_botao(COR_SECUNDARIA, COR_TEXTO)),
                                        ft.ElevatedButton("Excluir", on_click=lambda e, c=cliente: excluir_cliente(c), style=estilo_botao(COR_ALERTA)),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        **estilo_card(),
                    )
                )
        else:
            lista_clientes.controls.append(
                ft.Text("Nenhum cliente encontrado.", size=16, color=COR_ALERTA)
            )
        atualizar_conteudo_dinamico(
            ft.Column(
                [
                    ft.Text("Gerenciamento de Clientes", size=24, weight="bold", color=COR_PRIMARIA),
                    lista_clientes,
                    ft.ElevatedButton(
                        "Adicionar Cliente",
                        on_click=exibir_adicionar_cliente,
                        style=estilo_botao(),
                    ),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

    # Função para exibir o formulário de adição de cliente
    def exibir_adicionar_cliente(e=None):
        nome_input = ft.TextField(label="Nome", width=300)
        telefone_input = ft.TextField(label="Telefone", width=300)
        email_input = ft.TextField(label="Email", width=300)
        mensagem_erro = ft.Text("", color=COR_ALERTA, size=14)  # Texto para mostrar erros
        
        def validar_e_salvar_cliente(e):
            mensagem_erro.value = ""  # Limpa mensagem de erro anterior
            
            try:
                if not nome_input.value:
                    mensagem_erro.value = "Nome é obrigatório"
                    page.update()
                    return
                    
                # Validação do telefone
                if not telefone_input.value or not any(c.isdigit() for c in telefone_input.value):
                    mensagem_erro.value = "Telefone deve conter números"
                    page.update()
                    return
                    
                # Validação do email
                if not email_input.value or "@" not in email_input.value or "." not in email_input.value:
                    mensagem_erro.value = "Email inválido. Deve conter @ e ."
                    page.update()
                    return
                
                # Tenta adicionar o cliente
                hotel.adicionar_cliente(nome_input.value, telefone_input.value, email_input.value)
                exibir_mensagem("Cliente adicionado com sucesso!", COR_DESTAQUE)
                exibir_clientes(None)
                
            except ValueError as erro:
                mensagem_erro.value = str(erro)
                page.update()

        formulario_adicionar_cliente = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Adicionar Cliente", size=20, weight="bold", color=COR_PRIMARIA),
                    nome_input,
                    telefone_input,
                    email_input,
                    mensagem_erro,  # Adiciona o texto de erro ao formulário
                    ft.ElevatedButton(
                        "Salvar",
                        on_click=validar_e_salvar_cliente,
                        style=estilo_botao(),
                    ),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            **estilo_card(),
            width=400,
        )

        atualizar_conteudo_dinamico(
            ft.Column(
                [
                    formulario_adicionar_cliente,
                    ft.ElevatedButton(
                        "Voltar para Lista de Clientes",
                        on_click=lambda _: exibir_clientes(None),
                        style=estilo_botao(COR_SECUNDARIA, COR_TEXTO),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )


    # Função para exibir o formulário de edição de cliente
    def exibir_editar_cliente(cliente):
        nome_input = ft.TextField(label="Nome", value=cliente.nome, width=300)
        telefone_input = ft.TextField(label="Telefone", value=cliente.telefone, width=300)
        email_input = ft.TextField(label="Email", value=cliente.email, width=300)
        mensagem_erro = ft.Text("", color=COR_ALERTA, size=14)  # Texto para mostrar erros

        def validar_e_salvar_alteracoes(e):
            mensagem_erro.value = ""  # Limpa mensagem de erro anterior
            
            try:
                if not nome_input.value:
                    mensagem_erro.value = "Nome é obrigatório"
                    page.update()
                    return
                    
                # Validação do telefone
                if not telefone_input.value or not any(c.isdigit() for c in telefone_input.value):
                    mensagem_erro.value = "Telefone deve conter números"
                    page.update()
                    return
                    
                # Validação do email
                if not email_input.value or "@" not in email_input.value or "." not in email_input.value:
                    mensagem_erro.value = "Email inválido. Deve conter @ e ."
                    page.update()
                    return
                
                # Tenta editar o cliente
                hotel.editar_cliente(cliente.id, nome_input.value, telefone_input.value, email_input.value)
                exibir_mensagem("Cliente editado com sucesso!", COR_DESTAQUE)
                exibir_clientes(None)
                
            except ValueError as erro:
                mensagem_erro.value = str(erro)
                page.update()

        formulario_editar_cliente = ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Editando Cliente: {cliente.nome}", size=20, weight="bold", color=COR_PRIMARIA),
                    nome_input,
                    telefone_input,
                    email_input,
                    mensagem_erro,  # Adiciona o texto de erro ao formulário
                    ft.ElevatedButton(
                        "Salvar Alterações",
                        on_click=validar_e_salvar_alteracoes,
                        style=estilo_botao(),
                    ),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            **estilo_card(),
            width=400,
        )

        atualizar_conteudo_dinamico(
            ft.Column(
                [
                    formulario_editar_cliente,
                    ft.ElevatedButton(
                        "Voltar para Lista de Clientes",
                        on_click=lambda _: exibir_clientes(None),
                        style=estilo_botao(COR_SECUNDARIA, COR_TEXTO),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )


    # Função para excluir um cliente
    def excluir_cliente(cliente):
        try:
            hotel.excluir_cliente(cliente.id)
            exibir_mensagem("Cliente excluído com sucesso!", COR_DESTAQUE)
            exibir_clientes(None)
        except ValueError as e:
            exibir_mensagem(str(e))

    # Função para exibir a lista de reservas
    def exibir_reservas(e):
        lista_reservas = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=300,
            spacing=20,
            run_spacing=20,
        )
        if hotel.listar_reservas():
            for reserva in hotel.listar_reservas():
                lista_reservas.controls.append(
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(f"Reserva para {reserva.cliente.nome}", size=18, weight="bold", color=COR_PRIMARIA),
                                ft.Text(f"Quarto {reserva.quarto.numero}", color=COR_TEXTO),
                                ft.Text(f"Check-In: {reserva.checkIn.strftime('%d/%m/%Y')}", color=COR_TEXTO),
                                ft.Text(f"Check-Out: {reserva.checkOut.strftime('%d/%m/%Y')}", color=COR_TEXTO),
                                ft.Row(
                                    [
                                        ft.ElevatedButton("Editar", on_click=lambda e, r=reserva: exibir_editar_reserva(r), style=estilo_botao(COR_SECUNDARIA, COR_TEXTO)),
                                        ft.ElevatedButton("Cancelar", on_click=lambda e, r=reserva: cancelar_reserva(r), style=estilo_botao(COR_ALERTA)),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        **estilo_card(),
                    )
                )
        else:
            lista_reservas.controls.append(
                ft.Text("Nenhuma reserva encontrada.", size=16, color=COR_ALERTA)
            )
        
        atualizar_conteudo_dinamico(
            ft.Column(
                [
                    ft.Text("Gerenciamento de Reservas", size=24, weight="bold", color=COR_PRIMARIA),
                    lista_reservas,
                    ft.ElevatedButton(
                        "Nova Reserva",
                        on_click=exibir_formulario_reserva,
                        style=estilo_botao(),
                    ),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

    # Função para exibir o formulário de reserva
    def exibir_formulario_reserva(e):
        cliente_dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(cliente.nome) for cliente in hotel.listar_clientes()],
            label="Cliente",
            width=300,
        )
        tipo_quarto_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("Single"),
                ft.dropdown.Option("Double"),
                ft.dropdown.Option("Suite"),
            ],
            label="Tipo de Quarto",
            width=300,
        )
        quarto_dropdown = ft.Dropdown(
            label="Número do Quarto",
            width=300,
            disabled=True,
        )
        data_entrada = ft.TextField(label="Data de Entrada (DD/MM/AAAA)", width=300)
        data_saida = ft.TextField(label="Data de Saída (DD/MM/AAAA)", width=300)
        mensagem_erro = ft.Text("", color=COR_ALERTA)

        def atualizar_quartos_disponiveis(e):
            tipo_selecionado = tipo_quarto_dropdown.value
            quartos_disponiveis = [
                quarto for quarto in hotel.listar_quartos()
                if quarto.tipo == tipo_selecionado and quarto.disponibilidade == "Disponível"
            ]
            
            if not quartos_disponiveis:
                quarto_dropdown.disabled = True
                quarto_dropdown.options = []
                mensagem_erro.value = f"Não há quartos do tipo {tipo_selecionado} disponíveis."
            else:
                quarto_dropdown.disabled = False
                quarto_dropdown.options = [
                    ft.dropdown.Option(f"Quarto {quarto.numero}") for quarto in quartos_disponiveis
                ]
                mensagem_erro.value = ""
            
            page.update()

        tipo_quarto_dropdown.on_change = atualizar_quartos_disponiveis

        def realizar_reserva(e):
            try:
                cliente = hotel.obter_cliente_por_nome(cliente_dropdown.value)
                quarto = hotel.obter_quarto_por_numero(int(quarto_dropdown.value.split()[1]))
                data_entrada_obj = datetime.strptime(data_entrada.value, "%d/%m/%Y")
                data_saida_obj = datetime.strptime(data_saida.value, "%d/%m/%Y")
                hotel.realizar_reserva(cliente, quarto, data_entrada_obj, data_saida_obj, "Confirmada")
                exibir_mensagem("Reserva realizada com sucesso!", COR_DESTAQUE)
                exibir_reservas(None)
            except ValueError as erro:
                mensagem_erro.value = str(erro)
                page.update()

        formulario_reserva = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Nova Reserva", size=20, weight="bold", color=COR_PRIMARIA),
                    cliente_dropdown,
                    tipo_quarto_dropdown,
                    quarto_dropdown,
                    data_entrada,
                    data_saida,
                    mensagem_erro,
                    ft.ElevatedButton(
                        "Realizar Reserva",
                        on_click=realizar_reserva,
                        style=estilo_botao(),
                    ),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            **estilo_card(),
            width=400,
        )

        atualizar_conteudo_dinamico(
            ft.Column(
                [
                    formulario_reserva,
                    ft.ElevatedButton(
                        "Voltar para Lista de Reservas",
                        on_click=lambda _: exibir_reservas(None),
                        style=estilo_botao(COR_SECUNDARIA, COR_TEXTO),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

    # Função para exibir o formulário de edição de reserva
    def exibir_editar_reserva(reserva):
        quarto_dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(f"Quarto {quarto.numero}") for quarto in hotel.listar_quartos()],
            label="Quarto",
            width=300,
            value=f"Quarto {reserva.quarto.numero}",
        )
        data_entrada = ft.TextField(label="Nova Data de Entrada (DD/MM/AAAA)", value=reserva.checkIn.strftime("%d/%m/%Y"), width=300)
        data_saida = ft.TextField(label="Nova Data de Saída (DD/MM/AAAA)", value=reserva.checkOut.strftime("%d/%m/%Y"), width=300)
        mensagem_erro = ft.Text("", color=COR_ALERTA)

        def salvar_alteracoes(e):
            try:
                quarto = hotel.obter_quarto_por_numero(int(quarto_dropdown.value.split()[1]))
                nova_data_entrada = datetime.strptime(data_entrada.value, "%d/%m/%Y")
                nova_data_saida = datetime.strptime(data_saida.value, "%d/%m/%Y")
                hotel.editar_reserva(reserva, quarto, nova_data_entrada, nova_data_saida, "Confirmada")
                exibir_mensagem("Reserva editada com sucesso!", COR_DESTAQUE)
                exibir_reservas(None)
            except ValueError as erro:
                mensagem_erro.value = str(erro)
                page.update()

        formulario_editar_reserva = ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"Editando Reserva: {reserva.cliente.nome}", size=20, weight="bold", color=COR_PRIMARIA),
                    quarto_dropdown,
                    data_entrada,
                    data_saida,
                    mensagem_erro,
                    ft.ElevatedButton(
                        "Salvar Alterações",
                        on_click=salvar_alteracoes,
                        style=estilo_botao(),
                    ),
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            **estilo_card(),
            width=400,
        )

        atualizar_conteudo_dinamico(
            ft.Column(
                [
                    formulario_editar_reserva,
                    ft.ElevatedButton(
                        "Voltar para Lista de Reservas",
                        on_click=lambda _: exibir_reservas(None),
                        style=estilo_botao(COR_SECUNDARIA, COR_TEXTO),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )
        )

    # Função para cancelar uma reserva
    def cancelar_reserva(reserva):
        try:
            hotel.cancelar_reserva(reserva)
            exibir_mensagem("Reserva cancelada com sucesso!", COR_DESTAQUE)
            exibir_reservas(None)
        except ValueError as e:
            exibir_mensagem(str(e))

    def mudar_nav_ativa(e):
        for item in nav_items:
            item.bgcolor = None
        e.control.bgcolor = COR_SECUNDARIA
        page.update()

    def navegar(e, destino):
        mudar_nav_ativa(e)
        if destino == "inicio":
            exibir_quartos(None)
        elif destino == "clientes":
            exibir_clientes(None)
        elif destino == "reservas":
            exibir_reservas(None)

    nav_items = [
        ft.Container(
            content=ft.Text("Início", size=16, color=COR_TEXTO),
            padding=10,
            bgcolor=COR_SECUNDARIA,
            border_radius=8,
            on_click=lambda e: navegar(e, "inicio"),
        ),
        ft.Container(
            content=ft.Text("Gerenciar Clientes", size=16, color=COR_TEXTO),
            padding=10,
            bgcolor=None,
            border_radius=8,
            on_click=lambda e: navegar(e, "clientes"),
        ),
        ft.Container(
            content=ft.Text("Gerenciar Reservas", size=16, color=COR_TEXTO),
            padding=10,
            bgcolor=None,
            border_radius=8,
            on_click=lambda e: navegar(e, "reservas"),
        ),
    ]

    header = ft.Container(
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Icon(ft.Icons.HOTEL, size=30, color=COR_PRIMARIA),
                        ft.Text(hotel.nomeHotel, size=24, weight="bold", color=COR_PRIMARIA),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(nav_items, alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=20,
        bgcolor="white",
        border=ft.border.only(bottom=ft.border.BorderSide(1, COR_SECUNDARIA)),
    )

    conteudo_dinamico = ft.Container(
        content=ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
        padding=20,
    )

    page.add(
        ft.Column(
            [
                header,
                conteudo_dinamico,
            ],
            spacing=0,
            expand=True,
        )
    )

    exibir_quartos(None)

ft.app(target=main)
