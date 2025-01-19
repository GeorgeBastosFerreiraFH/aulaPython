import flet as ft

def main(page: ft.Page):
      
    theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.AMBER_100,
            secondary=ft.colors.BLUE_ACCENT_100,
            background=ft.colors.WHITE,
            surface=ft.colors.GREY,
            on_primary=ft.colors.DEEP_ORANGE_ACCENT_200,
            on_secondary=ft.colors.BLACK,
            on_background=ft.colors.BLACK,
            on_surface=ft.colors.BLACK
        )
    )
    
    page.theme = theme
    
    page.add(    
        ft.Row(
            [
                ft.Text("Texto Personalizado", color="primary", bgcolor="background"),
                ft.FilledButton("CLIQUE AQUI", color="secondary", bgcolor="background")
            ]
        )
    )
    
ft.app(target=main)