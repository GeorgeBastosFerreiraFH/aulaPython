import flet as ft

def main(page: ft.Page):
    
    def data_formatada(data):

        dataFormatada = ''.join(filter(str.isdigit, data.control.value))
        
        if len(dataFormatada) > 2:
            dataFormatada = dataFormatada[:2] + '/' + dataFormatada[2:]
        if len(dataFormatada) > 5:
            dataFormatada = dataFormatada[:5] + '/' + dataFormatada[5:]
        
        dataFormatada = dataFormatada[:10]
        
        data.control.value = dataFormatada
        data.control.update()
        
    def telefone_formatado(telefone):

        telefoneFormatado = ''.join(filter(str.isdigit, telefone.control.value))

        if len(telefoneFormatado) > 2:
            telefoneFormatado = '(' + telefoneFormatado[:2] + ') ' + telefoneFormatado[2:]
        if len(telefoneFormatado) > 10:
            telefoneFormatado = telefoneFormatado[:10] + '-' + telefoneFormatado[10:]

        telefoneFormatado = telefoneFormatado[:15]

        telefone.control.value = telefoneFormatado
        telefone.control.update()
                
    def btn_click(e):
        
        for campo in [txt_nome, txt_sobrenome, txt_telefone, txt_email, txt_data_nasc, txt_senha, txt_confirm_senha]:
            campo.error_text = ""
            
        if not txt_nome.value:
            txt_nome.error_text = "Por favor, digite seu nome"
            page.update()
        elif not txt_sobrenome.value:
            txt_sobrenome.error_text = "Por favor, digite seu sobrenome"
            page.update()
        elif not txt_telefone.value:
            txt_telefone.error_text = "Por favor, digite seu telefone"
            page.update()
        elif not txt_email.value:
            txt_email.error_text = "Por favor, digite seu e-mail"
            page.update()
        elif not txt_data_nasc.value:
            txt_data_nasc.error_text = "Por favor, digite sua data de nascimento"
            page.update()
        elif not txt_senha.value:
            txt_senha.error_text = "Por favor, digite sua senha"
            page.update()
        elif not txt_confirm_senha.value:
            txt_confirm_senha.error_text = "Por favor, confirme sua senha"
            page.update()
        elif txt_senha.value != txt_confirm_senha.value:
            txt_confirm_senha.error_text = "As senhas não coincidem"
            txt_confirm_senha.focus()
            page.update()
        elif len(txt_senha.value) < 8:
            txt_senha.error_text = "A senha deve ter no mínimo 8 caracteres"
            txt_confirm_senha.focus()
            page.update()
        else:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Cadastro realizado com sucesso!"),
                open=True,
                bgcolor=ft.colors.GREEN,
            )
            page.snack_bar.open = True
            page.update()
            return
        
        page.update()
      

    page.title = "Formulário de Cadastro"
    page.scroll = ft.ScrollMode.HIDDEN

    txt_nome = ft.TextField(label="Nome", hint_text="Digite seu nome", bgcolor='WHITE60')
    txt_sobrenome = ft.TextField(label="Sobrenome", hint_text="Digite seu sobrenome", bgcolor='WHITE60')
    txt_email = ft.TextField(label="E-mail", hint_text="Digite seu e-mail", bgcolor='WHITE60')
    txt_telefone = ft.TextField(label="Telefone", hint_text="Digite seu telefone", on_change=telefone_formatado, bgcolor='WHITE60')
    txt_data_nasc = ft.TextField(label="Data de Nascimento", hint_text="Digite sua data de nascimento", on_change=data_formatada, bgcolor='WHITE60')
    txt_senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, hint_text="Digite sua senha", bgcolor='WHITE60')
    txt_confirm_senha = ft.TextField(label="Confirme sua senha", password=True, can_reveal_password=True, hint_text="Confirme sua senha", bgcolor='WHITE60')
                
    page.add(
        ft.Card(
            elevation=10,
            margin=ft.margin.all(20),
            content=ft.Container(
                bgcolor=ft.colors.SECONDARY,
                shadow=ft.BoxShadow(spread_radius=5, blur_radius=10, color=ft.colors.BLACK26),
                border_radius=ft.border_radius.all(10),
                border=ft.border.all(1, ft.colors.BLACK),
                padding=20,
                    content = ft.Column(
                        controls=[
                            ft.Text("Formulário de Cadastro", size=24, weight="bold", color=ft.colors.WHITE),
                            txt_nome,
                            txt_sobrenome,
                            txt_telefone,
                            txt_email,
                            txt_data_nasc,

                            ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                                ft.Text("Crie uma senha", size=15, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                txt_senha,
                                txt_confirm_senha,

                            ft.Row(
                                [
                                    ft.FilledButton("Cadastrar", on_click=btn_click),
                                    ft.ElevatedButton("Sair", on_click=lambda _: page.window_close()),
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                ),
                            ],
                        spacing=10,
                        ),
                    )
                )
            )


ft.app(target=main)