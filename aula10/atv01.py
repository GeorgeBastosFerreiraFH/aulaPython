import flet as ft

def main(page: ft.Page):
    
    page.bgcolor = ft.colors.BLACK
    
    page.add(
        ft.Text("Seja Bem vindo!", size=30, color=ft.colors.YELLOW, weight=ft.FontWeight.W_500),
        ft.Text("Esse é o meu primeiro aplicativo com Flet", size=10, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
        ft.Text("Vamos começar?", color=ft.colors.RED, size=50, weight=ft.FontWeight.BOLD),
    )

ft.app(target=main)
