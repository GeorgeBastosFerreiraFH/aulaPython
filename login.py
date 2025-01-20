import flet as ft

def main(page: ft.Page):
    page.title = "Tela de Login/Senha"
    page.scroll = ft.ScrollMode.HIDDEN
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.BLUE_GREY_50

    inputLogin = ft.TextField(label="Login", 
                              color=ft.Colors.BLACK,
                              label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                              hint_text="Digite seu login", 
                              hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                              border_color=ft.Colors.BLACK)
    
    inputSenha = ft.TextField(label="Senha",
                              color=ft.Colors.BLACK,
                              label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                              hint_text="Digite sua senha", 
                              hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                              border_color=ft.Colors.BLACK,
                              can_reveal_password=True,
                              password=True)
    
    btnLogar = ft.ElevatedButton("Login", 
                                color=ft.Colors.BLACK,
                                width=200,
                                height=50,

                                style=ft.ButtonStyle(
                                    text_style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                    )                                    
                                ),
                               )

    esqueciSenha = ft.TextButton("Esqueci minha senha", 
                                 style=ft.ButtonStyle(color=ft.Colors.BLACK)
                                 )


    # def btnLogar(e):
    #     if not inputLogin.value:
    #         inputLogin.errorText = "Por favor, digite seu login"
    #         page.update()
    #     elif not inputSenha.value:
    #         inputSenha.erroText = "Por favor, digite sua senha"
    #     else:
    #         page.snack_bar = ft.SnackBar(
    #             content=ft.Text("Login realizado com sucesso!"),
    #             open=True,
    #             bgcolor=ft.colors.GREEN,
    #         )
    #         page.snack_bar.open = True
    #         page.update()
    #         return
        
    #     page.update()


    page.add(
    
        ft.Column(
            [
                ft.Text("Login", size=24, weight="bold", color=ft.colors.GREY, text_align="CENTER"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        ft.Card(
                    elevation=10,
                    margin=ft.margin.all(50),
                    content=ft.Container(
                        bgcolor=ft.colors.WHITE,
                        shadow=ft.BoxShadow(spread_radius=5, blur_radius=10, color=ft.colors.BLACK26),
                        border_radius=ft.border_radius.all(10),
                        border=ft.border.all(1, ft.colors.BLACK),
                        padding=20,
                            content = ft.Column(
                                controls=[
                                    
                                    inputLogin,
                                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                                    inputSenha,
                                    ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                                    ],
                                spacing=10,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),

                            ),
                            
                        ),
                    ft.Column(
                            [
                                btnLogar,
                                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                                esqueciSenha,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),

                    )
                

ft.app(target=main)
