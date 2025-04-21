import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[ft.Text("Thank you"), ft.Button(text="Hello")],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
    )


ft.app(main)
