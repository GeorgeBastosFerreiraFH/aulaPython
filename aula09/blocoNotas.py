import flet as ft

def exibirBarraStatus(barraStatus, mensagem, page):
    barraStatus.value = mensagem
    page.update()

def abrirArquivo(nomeArquivo, painelArquivos, barraStatus, areaTexto, page, rodape):
    for controle in painelArquivos.controls:
        if isinstance(controle, ft.Row):
            if nomeArquivo == controle.controls[0].value:
                with open(nomeArquivo, "r") as arquivo:
                    conteudo = arquivo.read()
                areaTexto.value = conteudo
                exibirBarraStatus(barraStatus, f"Arquivo '{nomeArquivo}' aberto para leitura.", page)
                break
            else:
                exibirBarraStatus(barraStatus, f"Arquivo '{nomeArquivo}' não encontrado.", page)
    rodape.visible = False
    page.update()

def editarTexto(nomeArquivo, areaTexto, painelArquivos, barraStatus, page, rodape):
    with open(nomeArquivo, "r") as arquivo:
        conteudo = arquivo.read()
    areaTexto.value = conteudo
    exibirBarraStatus(barraStatus, f"Arquivo '{nomeArquivo}' em modo de edição.", page)
    
    rodape.controls[1].controls[0].value = nomeArquivo
    rodape.controls[1].controls[1].on_click = lambda _: salvarEdicao(nomeArquivo, areaTexto, painelArquivos, barraStatus, page, rodape)
    rodape.visible = True
    areaTexto.focus()
    page.update()

def salvarEdicao(nomeArquivo, areaTexto, painelArquivos, barraStatus, page, rodape):
    with open(nomeArquivo, "w") as arquivo:
        arquivo.write(areaTexto.value)
    exibirBarraStatus(barraStatus, f"Arquivo '{nomeArquivo}' salvo com sucesso!", page)
    rodape.visible = False
    areaTexto.value = ""
    page.update()

def excluirArquivo(nomeArquivo, areaTexto, painelArquivos, barraStatus, page, rodape):
    for controle in painelArquivos.controls:
        if isinstance(controle, ft.Row) and controle.controls[0].value == nomeArquivo:
            painelArquivos.controls.remove(controle)
            break
    exibirBarraStatus(barraStatus, f"Arquivo '{nomeArquivo}' excluído.", page)
    rodape.visible = False
    areaTexto.value = ""
    page.update()

def salvarArquivo(e, areaTexto, painelArquivos, barraStatus, page, rodape):
    
    if not areaTexto.value.strip():
        exibirBarraStatus(barraStatus, "Nenhum texto para salvar!", page)
        return
  
    
    rodape.controls[1].controls[0].value = ""
    rodape.controls[1].controls[1].on_click = lambda _: salvarArquivoComNome(areaTexto, painelArquivos, barraStatus, page, rodape)
    rodape.visible = True
    barraStatus.value = ""
    page.update()

def salvarArquivoComNome(areaTexto, painelArquivos, barraStatus, page, rodape):
    nomeArquivo = rodape.controls[1].controls[0].value.strip()    
    if nomeArquivo:
        with open(nomeArquivo, "w") as arquivo:
            arquivo.write(areaTexto.value)
        adicionarArquivoNaLista(nomeArquivo, painelArquivos, areaTexto, barraStatus, page, rodape)
        exibirBarraStatus(barraStatus, f"Arquivo '{nomeArquivo}' salvo com sucesso!", page)
        rodape.visible = False
    else:
        exibirBarraStatus(barraStatus, "Nome de arquivo inválido!", page)
    areaTexto.value = ""
    page.update()

def adicionarArquivoNaLista(nomeArquivo, painelArquivos, areaTexto, barraStatus, page, rodape):
    for controle in painelArquivos.controls:
        if isinstance(controle, ft.Row) and controle.controls[0].value == nomeArquivo:
            return
    
    painelArquivos.controls.append(
        ft.Row(
            controls=[
                ft.Text(nomeArquivo, size=12),
                ft.IconButton(icon=ft.icons.FOLDER_OPEN, tooltip="Abrir", on_click=lambda _: abrirArquivo(nomeArquivo, painelArquivos, barraStatus, areaTexto, page, rodape)),
                ft.IconButton(icon=ft.icons.EDIT, tooltip="Editar", on_click=lambda _: editarTexto(nomeArquivo, areaTexto, painelArquivos, barraStatus, page, rodape)),
                ft.IconButton(icon=ft.icons.DELETE, tooltip="Excluir", on_click=lambda _: excluirArquivo(nomeArquivo, areaTexto, painelArquivos, barraStatus, page, rodape)),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,
        )
    )
    page.update()

def aplicarNegrito(e, areaTexto, barraStatus, page):
    areaTexto.value = f"<b>{areaTexto.value}</b>"
    exibirBarraStatus(barraStatus, "Texto em negrito aplicado!", page)
    page.update()

def aplicarItalico(e, areaTexto, barraStatus, page):
    areaTexto.value = f"<i>{areaTexto.value}</i>"
    exibirBarraStatus(barraStatus, "Texto em itálico aplicado!", page)
    page.update()

def aumentarFonte(e, areaTexto, barraStatus, page):
    areaTexto.text_size += 2
    exibirBarraStatus(barraStatus, f"Fonte aumentada para {areaTexto.text_size}px", page)
    page.update()

def diminuirFonte(e, areaTexto, barraStatus, page):
    if areaTexto.text_size > 8:
        areaTexto.text_size -= 2
        exibirBarraStatus(barraStatus, f"Fonte diminuída para {areaTexto.text_size}px", page)
        page.update()

def novoDocumento(areaTexto, barraStatus, page, rodape):
    areaTexto.value = ""
    rodape.visible = False
    exibirBarraStatus(barraStatus, "Novo documento criado", page)
    page.update()
    
def contadorPalavras(areaTexto, barraStatus, page):
    palavras = areaTexto.value.split()
    exibirBarraStatus(barraStatus, f"Total de palavras: {len(palavras)}", page)
    page.update()

def main(page: ft.Page):
    barraStatus = ft.Text(value="")

    areaTexto = ft.TextField(
        multiline=True,
        expand=True,
        hint_text="Escreva aqui...",
        text_size=14,
        min_lines=50,
        max_lines=50,
    )

    rodape = ft.Column(
        controls=[
            ft.Text("Escolha o nome do arquivo:", size=14),
            ft.Row(
                controls=[
                    ft.TextField(hint_text="Nome do arquivo...", expand=True),
                    ft.IconButton(icon=ft.icons.SAVE, tooltip="Salvar"),
                ],
            ),
        ],
        visible=False,
    )

    menuLateral = ft.Column(
        controls=[
            ft.Row(
                controls=[ft.IconButton(icon=ft.icons.NOTE_ADD, tooltip="Novo Documento", on_click=lambda _: novoDocumento(areaTexto, barraStatus, page, rodape)), ft.Text("Novo Documento", size=12)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            ft.Row(
                controls=[ft.IconButton(icon=ft.icons.SAVE, tooltip="Salvar", on_click=lambda e: salvarArquivo(e, areaTexto, painelArquivos, barraStatus, page, rodape)), ft.Text("Salvar", size=12)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            ft.Row(
                controls=[ft.IconButton(icon=ft.icons.FORMAT_BOLD, tooltip="Negrito", on_click=lambda e: aplicarNegrito(e, areaTexto, barraStatus, page)), ft.Text("Negrito", size=12)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            ft.Row(
                controls=[ft.IconButton(icon=ft.icons.FORMAT_ITALIC, tooltip="Itálico", on_click=lambda e: aplicarItalico(e, areaTexto, barraStatus, page)), ft.Text("Itálico", size=12)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            ft.Row(
                controls=[ft.IconButton(icon=ft.icons.ZOOM_IN, tooltip="Aumentar Fonte", on_click=lambda e: aumentarFonte(e, areaTexto, barraStatus, page)), ft.Text("Aumentar Fonte", size=12)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            ft.Row(
                controls=[ft.IconButton(icon=ft.icons.ZOOM_OUT, tooltip="Diminuir Fonte", on_click=lambda e: diminuirFonte(e, areaTexto, barraStatus, page)), ft.Text("Diminuir Fonte", size=12)],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    painelArquivos = ft.Column(
        controls=[ft.Text("Arquivos Salvos", size=16)],
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
    )

    page.add(
        ft.Row(
            controls=[
                menuLateral,
                ft.VerticalDivider(width=1),
                ft.Column(controls=[areaTexto, rodape, barraStatus], expand=True),
                ft.VerticalDivider(width=1),
                painelArquivos,
            ],
            expand=True,
        )
    )

    page.update()

ft.app(target=main)

