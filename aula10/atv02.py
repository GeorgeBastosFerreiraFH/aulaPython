import flet as ft

def main(page: ft.Page):
    
    page.bgcolor = ft.colors.BLACK
    page.scroll = ft.ScrollMode.HIDDEN
    
    
    def criarBotao(texto, cor, bgcor, largura, altura, tamanho):
        return ft.ElevatedButton(
            text=texto,
            color=cor,
            bgcolor=bgcor,
            width=largura,
            height=altura,
            style=ft.ButtonStyle(
                shape={"": ft.RoundedRectangleBorder(radius=tamanho)},
            ),
        )

        
       
    page.add(
        ft.Row(
            [
                criarBotao("Laranja", ft.colors.WHITE, ft.colors.AMBER, 100, 50, 10),
                criarBotao("Azul", ft.colors.WHITE, ft.colors.BLUE, 100, 50, 20),
                criarBotao("Vermelho", ft.colors.BLACK, ft.colors.RED, 150, 200, 30),
            ]
        ),
    )

ft.app(target=main)
