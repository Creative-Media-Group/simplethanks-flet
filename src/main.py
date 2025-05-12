import flet as ft
import flet_audio as fta
from localisation import (
    BIRTHDAY,
    DESCRIPTION,
    FATHERSDAY,
    FORMALNAME,
    HAPPYFATHERSDAY,
    HAPPYMOTHERSDAY,
    MOTHERSDAY,
    SUPPORTEDPLATFORM,
    THANKYOU,
)


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


def play(audio_obj: ft.Control):
    audio_obj.play()


def main(page: ft.Page):
    def on_resized(e):
        page.update()

    page.adaptive = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.on_resized = on_resized
    # page.scroll = ft.ScrollMode.AUTO
    # page.expand = True
    audio1 = fta.Audio(
        src="happy-birthday-whistled.wav",
    )
    page.appbar = ft.AppBar(title=ft.Text("Simple Thanks"))
    page.overlay.append(audio1)
    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[ft.Text(THANKYOU(page=page))],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[
                            mybutton(
                                text=BIRTHDAY(page=page),
                                on_click=lambda _: play(audio_obj=audio1),
                                width=page.width * 0.5,
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            mybutton(
                                text=MOTHERSDAY(page=page),
                                on_click=lambda _: print(MOTHERSDAY(page=page)),
                                width=page.width * 0.5,
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            mybutton(
                                text=FATHERSDAY(page=page),
                                on_click=lambda _: print(FATHERSDAY(page=page)),
                                width=page.width * 0.5,
                            )
                        ]
                    ),
                    ft.Row(
                        controls=[
                            mybutton(
                                text="Website",
                                on_click=lambda _: print("Mothers Day"),
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
