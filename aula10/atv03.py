import flet as ft

def main(page: ft.Page):
    page.title = "Formulário Estilizado"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Container(
                content=ft.Column(
                    [
                        ft.TextField(label="Nome", hint_text="Digite seu nome", bgcolor="WHITE60"),
                        ft.TextField(label="E-mail", hint_text="Digite seu e-mail", bgcolor='WHITE60'), 
                            
                        ft.Row([
                                
                                ft.ElevatedButton("Enviar"),
                                ], 
                            alignment=ft.MainAxisAlignment.START),

                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.START,
                    expand=True
                ),
                width=500,
                margin=ft.margin.all(20),
                padding=30,
                bgcolor=ft.colors.WHITE,
                border_radius=20,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.colors.BLUE_GREY_300,
                    offset=ft.Offset(0, 0),
                    blur_style=ft.ShadowBlurStyle.OUTER,
                )
            )
        )

ft.app(target=main)