import flet as ft


def mybutton(text: str, on_click, width: int, disabled: bool = False):
    return ft.ElevatedButton(
        content=ft.Text(text, size=20),
        height=50,
        width=width,
        on_click=on_click,
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.RED,
            ft.ControlState.PRESSED: ft.Colors.TRANSPARENT,
        },
        expand=True,
        disabled=disabled,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )


def play():
    pass


def main(page: ft.Page):
    def on_resized(e):
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_resized = on_resized
    # page.scroll = ft.ScrollMode.AUTO
    # page.expand = True
    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[ft.Text("Thank you")],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[
                            mybutton(
                                text="Happy Birthday",
                                on_click=lambda _: play(),
                                width=page.width * 0.5,
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            mybutton(
                                text="Mothers Day",
                                on_click=lambda _: play(),
                                width=page.width * 0.5,
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            mybutton(
                                text="Fathers Day",
                                on_click=lambda _: play(),
                                width=page.width * 0.5,
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            mybutton(
                                text="Website",
                                on_click=lambda _: play(),
                                width=page.width * 0.5,
                            )
                        ]
                    ),
                ],
                # width=page.width * 0.5,
                # scroll=True,
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
    )


ft.app(main)
