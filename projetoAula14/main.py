import flet as ft
from datetime import datetime
from hotel import *

def main(page: ft.Page):
    page.title = "Sistema de Gerenciamento Hoteleiro"
    page.theme_mode = "light"
    page.padding = 20
    page.spacing = 20
    
    def create_header(title):
        return ft.Container(
            content=ft.Column([
                ft.Divider(height=1, color=ft.colors.BLUE_GREY_100),
                ft.Text(title, size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900),
                ft.Divider(height=1, color=ft.colors.BLUE_GREY_100),
            ]),
            margin=ft.margin.only(bottom=20)
        )

    # Tela Inicial
    def view_home():
        return ft.Container(
            content=ft.Column([
                create_header("Sistema de Gerenciamento Hoteleiro"),
                
                # Menu de Navegação
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Nova Reserva",
                                icon=ft.icons.ADD_CIRCLE,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    color=ft.colors.WHITE,
                                ),
                                bgcolor=ft.colors.BLUE_700,
                            ),
                            ft.ElevatedButton(
                                text="Visualizar Reservas",
                                icon=ft.icons.CALENDAR_MONTH,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    color=ft.colors.WHITE,
                                ),
                                bgcolor=ft.colors.INDIGO_700,
                            ),
                            ft.ElevatedButton(
                                text="Gerenciar Clientes",
                                icon=ft.icons.PEOPLE_ALT,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    color=ft.colors.WHITE,
                                ),
                                bgcolor=ft.colors.DEEP_PURPLE_700,
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=10,
                        color=ft.colors.BLUE_GREY_100,
                    )
                ),
                
                # Lista de Quartos
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Quartos Disponíveis",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE_900
                        ),
                        ft.GridView(
                            runs_count=3,
                            max_extent=300,
                            spacing=20,
                            run_spacing=20,
                            controls=[
                                ft.Container(
                                    content=ft.Column([
                                        ft.Stack([
                                            ft.Container(
                                                content=ft.Image(
                                                    src="https://placeholder.com/300x200",
                                                    fit=ft.ImageFit.COVER,
                                                    border_radius=ft.border_radius.only(
                                                        top_left=8,
                                                        top_right=8
                                                    )
                                                ),
                                                height=150,
                                            ),
                                            ft.Container(
                                                content=ft.Text(
                                                    "DISPONÍVEL" if i % 2 == 0 else "OCUPADO",
                                                    color=ft.colors.WHITE,
                                                    weight=ft.FontWeight.BOLD,
                                                    size=12
                                                ),
                                                padding=8,
                                                margin=10,
                                                bgcolor=ft.colors.GREEN_700 if i % 2 == 0 else ft.colors.RED_700,
                                                border_radius=20,
                                                alignment=ft.alignment.center,
                                            )
                                        ]),
                                        ft.Container(
                                            content=ft.Column([
                                                ft.Text(
                                                    f"Quarto {101 + i}",
                                                    size=18,
                                                    weight=ft.FontWeight.BOLD
                                                ),
                                                ft.Text(
                                                    "Standard" if i < 2 else "Luxo",
                                                    size=14,
                                                    color=ft.colors.BLUE_GREY_700
                                                ),
                                                ft.Text(
                                                    f"R$ {200 if i < 2 else 400},00/noite",
                                                    size=16,
                                                    color=ft.colors.BLUE_700,
                                                    weight=ft.FontWeight.BOLD
                                                ),
                                            ]),
                                            padding=15
                                        )
                                    ]),
                                    bgcolor=ft.colors.WHITE,
                                    border_radius=8,
                                    shadow=ft.BoxShadow(
                                        spread_radius=1,
                                        blur_radius=10,
                                        color=ft.colors.BLUE_GREY_100,
                                    ),
                                )
                                for i in range(6)
                            ]
                        )
                    ]),
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    margin=ft.margin.only(top=20),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=10,
                        color=ft.colors.BLUE_GREY_100,
                    )
                )
            ])
        )

    # Tela de Reservas
    def view_reservas():
        return ft.Container(
            content=ft.Column([
                create_header("Reservas Ativas"),
                ft.ListView(
                    controls=[
                        ft.Container(
                            content=ft.Column([
                                ft.Row([
                                    ft.Column([
                                        ft.Text(
                                            f"Reserva #{i+1:03d}",
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.colors.BLUE_900
                                        ),
                                        ft.Text(
                                            "João Silva" if i % 2 == 0 else "Maria Santos",
                                            size=16
                                        ),
                                    ], expand=True),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE_OUTLINE,
                                        icon_color=ft.colors.RED_400,
                                        icon_size=20,
                                        tooltip="Cancelar Reserva"
                                    )
                                ]),
                                ft.Divider(),
                                ft.Row([
                                    ft.Column([
                                        ft.Text("Check-in"),
                                        ft.Text(
                                            "10/02/2025",
                                            color=ft.colors.BLUE_GREY_700
                                        )
                                    ]),
                                    ft.Column([
                                        ft.Text("Check-out"),
                                        ft.Text(
                                            "15/02/2025",
                                            color=ft.colors.BLUE_GREY_700
                                        )
                                    ]),
                                    ft.Column([
                                        ft.Text("Quarto"),
                                        ft.Text(
                                            f"{101 + i}",
                                            color=ft.colors.BLUE_GREY_700
                                        )
                                    ]),
                                    ft.Column([
                                        ft.Text("Valor Total"),
                                        ft.Text(
                                            "R$ 1.000,00",
                                            color=ft.colors.BLUE_700,
                                            weight=ft.FontWeight.BOLD
                                        )
                                    ]),
                                ], spacing=40)
                            ]),
                            padding=20,
                            bgcolor=ft.colors.WHITE,
                            border_radius=8,
                            margin=ft.margin.only(bottom=10),
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=10,
                                color=ft.colors.BLUE_GREY_100,
                            )
                        )
                        for i in range(5)
                    ],
                    spacing=10,
                )
            ])
        )

    # Formulário de Nova Reserva
    def view_nova_reserva():
        return ft.Container(
            content=ft.Column([
                create_header("Nova Reserva"),
                ft.Container(
                    content=ft.Column([
                        ft.Dropdown(
                            label="Cliente",
                            hint_text="Selecione o cliente",
                            options=[
                                ft.dropdown.Option("João Silva"),
                                ft.dropdown.Option("Maria Santos"),
                            ],
                            width=400,
                        ),
                        ft.Dropdown(
                            label="Quarto",
                            hint_text="Selecione o quarto",
                            options=[
                                ft.dropdown.Option("101 - Standard (R$ 200/noite)"),
                                ft.dropdown.Option("102 - Standard (R$ 200/noite)"),
                                ft.dropdown.Option("201 - Luxo (R$ 400/noite)"),
                            ],
                            width=400,
                        ),
                        ft.Row([
                            ft.TextField(
                                label="Check-in",
                                hint_text="Selecione a data",
                                prefix_icon=ft.icons.CALENDAR_TODAY,
                                read_only=True,
                                width=190,
                            ),
                            ft.IconButton(
                                icon=ft.icons.CALENDAR_MONTH,
                                icon_color=ft.colors.BLUE,
                            ),
                            ft.TextField(
                                label="Check-out",
                                hint_text="Selecione a data",
                                prefix_icon=ft.icons.CALENDAR_TODAY,
                                read_only=True,
                                width=190,
                            ),
                            ft.IconButton(
                                icon=ft.icons.CALENDAR_MONTH,
                                icon_color=ft.colors.BLUE,
                            ),
                        ]),
                        ft.Container(
                            content=ft.ElevatedButton(
                                text="Confirmar Reserva",
                                icon=ft.icons.CHECK_CIRCLE,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    color=ft.colors.WHITE,
                                ),
                                bgcolor=ft.colors.GREEN_700,
                            ),
                            margin=ft.margin.only(top=20),
                        )
                    ]),
                    padding=30,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=10,
                        color=ft.colors.BLUE_GREY_100,
                    )
                )
            ])
        )

    # Gerenciamento de Clientes
    def view_clientes():
        return ft.Container(
            content=ft.Column([
                create_header("Gerenciamento de Clientes"),
                
                # Formulário de Novo Cliente
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Novo Cliente",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE_900
                        ),
                        ft.Row([
                            ft.TextField(
                                label="Nome",
                                hint_text="Nome completo",
                                prefix_icon=ft.icons.PERSON,
                                expand=True
                            ),
                            ft.TextField(
                                label="CPF",
                                hint_text="000.000.000-00",
                                prefix_icon=ft.icons.NUMBERS,
                                width=200
                            ),
                            ft.TextField(
                                label="Telefone",
                                hint_text="(00) 00000-0000",
                                prefix_icon=ft.icons.PHONE,
                                width=200
                            ),
                        ]),
                        ft.Container(
                            content=ft.ElevatedButton(
                                text="Adicionar Cliente",
                                icon=ft.icons.PERSON_ADD,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8),
                                    color=ft.colors.WHITE,
                                ),
                                bgcolor=ft.colors.GREEN_700,
                            ),
                            margin=ft.margin.only(top=20),
                        )
                    ]),
                    padding=30,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    margin=ft.margin.only(bottom=20),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=10,
                        color=ft.colors.BLUE_GREY_100,
                    )
                ),
                
                # Lista de Clientes
                ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Clientes Cadastrados",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE_900
                        ),
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(ft.Text("Nome")),
                                ft.DataColumn(ft.Text("CPF")),
                                ft.DataColumn(ft.Text("Telefone")),
                                ft.DataColumn(ft.Text("Ações")),
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("João Silva")),
                                        ft.DataCell(ft.Text("123.456.789-00")),
                                        ft.DataCell(ft.Text("(11) 99999-9999")),
                                        ft.DataCell(
                                            ft.Row([
                                                ft.IconButton(
                                                    icon=ft.icons.EDIT,
                                                    icon_color=ft.colors.BLUE,
                                                    icon_size=20,
                                                    tooltip="Editar"
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.DELETE,
                                                    icon_color=ft.colors.RED_400,
                                                    icon_size=20,
                                                    tooltip="Excluir"
                                                ),
                                            ])
                                        ),
                                    ]
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text("Maria Santos")),
                                        ft.DataCell(ft.Text("987.654.321-00")),
                                        ft.DataCell(ft.Text("(11) 88888-8888")),
                                        ft.DataCell(
                                            ft.Row([
                                                ft.IconButton(
                                                    icon=ft.icons.EDIT,
                                                    icon_color=ft.colors.BLUE,
                                                    icon_size=20,
                                                    tooltip="Editar"
                                                ),
                                                ft.IconButton(
                                                    icon=ft.icons.DELETE,
                                                    icon_color=ft.colors.RED_400,
                                                    icon_size=20,
                                                    tooltip="Excluir"
                                                ),
                                            ])
                                        ),
                                    ]
                                ),
                            ],
                        )
                    ]),
                    padding=30,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=10,
                        color=ft.colors.BLUE_GREY_100,
                    )
                )
            ])
        )

    # Sistema de navegação
    navigation_items = {
        "home": {"icon": ft.icons.HOME, "text": "Início", "view": view_home},
        "nova_reserva": {"icon": ft.icons.ADD_CIRCLE, "text": "Nova Reserva", "view": view_nova_reserva},
        "reservas": {"icon": ft.icons.CALENDAR_MONTH, "text": "Reservas", "view": view_reservas},
        "clientes": {"icon": ft.icons.PEOPLE, "text": "Clientes", "view": view_clientes},
    }

    def change_view(e):
        selected = e.control.selected_index
        content.content = list(navigation_items.values())[selected]["view"]()
        page.update()

    # Container principal para o conteúdo
    content = ft.Container(
        content=view_home(),
        padding=20
    )

    # Nova navegação usando BottomAppBar
    navigation_rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        destinations=[
            ft.NavigationRailDestination(
                icon=item["icon"],
                label=item["text"],
            ) for item in navigation_items.values()
        ],
        on_change=change_view,
    )

    # Layout principal
    page.add(
        ft.Row(
            [
                navigation_rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [content],
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                ),
            ],
            expand=True,
        )
    )

ft.app(target=main)