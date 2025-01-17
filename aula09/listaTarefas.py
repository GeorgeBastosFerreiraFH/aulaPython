import flet as ft

listaTarefas = dict()

def main(page: ft.Page):
    tarefa_editando = None

    def listar_tarefas():
        tarefas_container.controls.clear()
        if not listaTarefas:
            tarefas_container.controls.append(ft.Text("Nenhuma tarefa cadastrada!", size=16, italic=True))
        else:
            for tarefa, dados in listaTarefas.items():
                tarefas_container.controls.append(
                    ft.Card(
                        content=ft.Container(
                            content=ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text(tarefa, weight="bold", size=16),
                                            ft.Text(
                                                f"Descrição: {dados['Descrição']}\n"
                                                f"Prioridade: {dados['Prioridade']}\n"
                                                f"Categoria: {dados['Categoria']}",
                                                size=14,
                                                italic=True,
                                            ),
                                        ],
                                        expand=True,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Checkbox(
                                                value=dados.get("Concluída", False),
                                                on_change=lambda e, t=tarefa: atualizar_status(t, e.control.value),
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.EDIT,
                                                tooltip="Editar tarefa",
                                                on_click=lambda e, t=tarefa: editar_tarefa(t),
                                            ),
                                            ft.IconButton(
                                                icon=ft.icons.DELETE,
                                                tooltip="Remover tarefa",
                                                on_click=lambda e, t=tarefa: remover_tarefa(t),
                                            ),
                                        ]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            padding=10,
                        ),
                        elevation=2,
                        margin=ft.margin.symmetric(vertical=5),
                    )
                )
        tarefas_container.update()

    def atualizar_status(tarefa, status):
        listaTarefas[tarefa]["Concluída"] = status
        listar_tarefas()

    def remover_tarefa(tarefa):
        del listaTarefas[tarefa]
        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Tarefa '{tarefa}' removida com sucesso!"),
            open=True,
            bgcolor=ft.colors.RED,
        )
        listar_tarefas()
        page.update()

    def editar_tarefa(tarefa):
        nonlocal tarefa_editando
        tarefa_editando = tarefa
        nomeTarefa.value = tarefa
        descricaoTarefa.value = listaTarefas[tarefa]["Descrição"]
        prioridade.value = listaTarefas[tarefa]["Prioridade"]
        categoria.value = listaTarefas[tarefa]["Categoria"]
        concluida.value = listaTarefas[tarefa].get("Concluída", False)
        page.update()

    def btn_click(e):
        nonlocal tarefa_editando
        for campo in [nomeTarefa, descricaoTarefa, prioridade, categoria]:
            campo.error_text = ""

        if not nomeTarefa.value:
            nomeTarefa.error_text = "Por favor, digite o nome da tarefa"
        elif not descricaoTarefa.value:
            descricaoTarefa.error_text = "Por favor, digite a descrição da tarefa"
        elif not prioridade.value:
            prioridade.error_text = "Por favor, selecione a prioridade da tarefa"
        elif not categoria.value:
            categoria.error_text = "Por favor, selecione a categoria da tarefa"
        else:
            if tarefa_editando:
                del listaTarefas[tarefa_editando]  # Remover a tarefa antiga ao editar
            listaTarefas[nomeTarefa.value] = {
                "Descrição": descricaoTarefa.value,
                "Prioridade": prioridade.value,
                "Categoria": categoria.value,
                "Concluída": concluida.value,
            }
            tarefa_editando = None
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Tarefa salva com sucesso!"),
                open=True,
                bgcolor=ft.colors.GREEN,
            )
            for campo in [nomeTarefa, descricaoTarefa, prioridade, categoria]:
                campo.value = ""
            listar_tarefas()
        page.update()

    page.title = "Lista de Tarefas"
    page.scroll = ft.ScrollMode.ALWAYS

    nomeTarefa = ft.TextField(label="Nome", hint_text="Digite o nome da tarefa")
    descricaoTarefa = ft.TextField(label="Descrição", hint_text="Digite a descrição da tarefa", multiline=True)
    prioridade = ft.Dropdown(
        label="Prioridade",
        options=[ft.dropdown.Option("Alta"), ft.dropdown.Option("Média"), ft.dropdown.Option("Baixa")],
    )
    categoria = ft.Dropdown(
        label="Categoria",
        options=[ft.dropdown.Option("Trabalho"), ft.dropdown.Option("Estudos"), ft.dropdown.Option("Lazer")],
    )
    concluida = ft.Checkbox(label="Concluída")

    tarefas_container = ft.Column(spacing=10)

    page.add(
        ft.Card(
            elevation=5,
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Cadastrar/Editar Tarefa", size=20, weight="bold"),
                        nomeTarefa,
                        descricaoTarefa,
                        prioridade,
                        categoria,
                        concluida,
                        ft.ElevatedButton("Salvar", on_click=btn_click),
                    ],
                    spacing=10,
                ),
                padding=20,
            ),
        ),
        ft.Divider(),
        ft.Text("Lista de Tarefas", size=20, weight="bold"),
        tarefas_container,
    )
    listar_tarefas()

ft.app(target=main)
