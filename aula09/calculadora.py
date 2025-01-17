import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Calculadora Python"
    pagina.scroll = ft.ScrollMode.HIDDEN
    pagina.theme = ft.Theme(color_scheme=ft.ColorScheme(background=ft.colors.BLACK))
    pagina.padding = 0
    pagina.window_width = 400
    pagina.window_height = 600

    expressaoAtual = ""
    textoDisplay = ft.Text(value="0", color=ft.colors.BLACK, size=24)

    def atualizarDisplay():
        textoDisplay.value = expressaoAtual or "0"
        textoDisplay.update()

    def cliqueBotao(evento):
        nonlocal expressaoAtual
        valor = evento.control.text

        if valor == "C":
            expressaoAtual = ""
        elif valor == "<":
            expressaoAtual = expressaoAtual[:-1]
        elif valor == "=":
            try:
                expressaoAtual = str(eval(expressaoAtual))
            except Exception:
                expressaoAtual = "Erro"
        else:
            expressaoAtual += valor      

        atualizarDisplay()

    def tratarTeclado(evento):
        nonlocal expressaoAtual

        if evento.key in "0123456789":
            expressaoAtual += evento.key[-1]
        elif evento.key in ".+-*/%()":
            expressaoAtual += evento.key
        elif evento.key == ",":
            expressaoAtual += "."
        elif evento.key == "Backspace":
            expressaoAtual = expressaoAtual[:-1]
        elif evento.key == "Enter" or evento.key == "=":
            try:
                expressaoAtual = str(eval(expressaoAtual))
            except Exception:
                expressaoAtual = "Erro"
        elif evento.key == "Escape":
            expressaoAtual = ""

        atualizarDisplay()

    def criarBotao(rotulo, expandir=False, cor=ft.colors.WHITE):
        return ft.ElevatedButton(
            text=rotulo,
            on_click=cliqueBotao,
            expand=expandir,
            bgcolor=cor,
            color=ft.colors.BLACK,
            width=60,
            height=60,
            style=ft.ButtonStyle(
                shape={"": ft.RoundedRectangleBorder(radius=10)},
            ),
        )

    painelResultado = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    textoDisplay,
                ],
                alignment="end",
            ),
            border=ft.border.all(1, ft.colors.TRANSPARENT),
            border_radius=10,
            padding=20,
            alignment=ft.alignment.bottom_right,
        ),
        width=300,
        height=120,
        color=ft.colors.WHITE,
    )

    painelCalculadora = ft.Column(
        [
            ft.Row(
                [
                    criarBotao("C", cor=ft.colors.RED_200),
                    criarBotao("%"),
                    criarBotao("<"),
                    criarBotao("/", cor=ft.colors.ORANGE_300),
                ]
            ),
            ft.Row(
                [
                    criarBotao("7"),
                    criarBotao("8"),
                    criarBotao("9"),
                    criarBotao("*", cor=ft.colors.ORANGE_300),
                ]
            ),
            ft.Row(
                [
                    criarBotao("4"),
                    criarBotao("5"),
                    criarBotao("6"),
                    criarBotao("-", cor=ft.colors.ORANGE_300),
                ]
            ),
            ft.Row(
                [
                    criarBotao("1"),
                    criarBotao("2"),
                    criarBotao("3"),
                    criarBotao("+", cor=ft.colors.ORANGE_300),
                ]
            ),
            ft.Row(
                [
                    criarBotao("0", expandir=True),
                    criarBotao("."),
                    criarBotao("=", cor=ft.colors.GREEN_200),
                ]
            ),
        ],
        spacing=5,
    )

    pagina.on_keyboard_event = tratarTeclado

    pagina.add(
        ft.Card(
            elevation=10,
            margin=ft.margin.all(20),
            width=350,
            height=550,
            content=ft.Container(
                content=ft.Column(
                    [
                        painelResultado,
                        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                        painelCalculadora,
                    ]
                ),
                padding=20,
                bgcolor=ft.colors.BLACK87,
                border_radius=10,
            ),
        )
    )

ft.app(target=main)
