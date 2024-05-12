import flet as ft
import passgener_app_gui, logingener_app_gui, database_app_gui


def main(page: ft.Page):
    page.title = 'LoDaLo - Login Data Lord'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'light'

    classic_passgen_view = ft.Container(passgener_app_gui.PassGener(), expand=True)
    loggen_view = ft.Container(logingener_app_gui.LogGener(), expand=True)
    database_view = ft.Container(database_app_gui.DataBaseViewer(), expand=True)

    def refresh(_):
        body.controls = [loggen_view]
        body.update()
        body.controls = [database_view]
        body.update()

    def passgen(_):
        body.controls = [classic_passgen_view]
        body.update()

    def loggen(_):
        body.controls = [loggen_view]
        body.update()

    def database(_):
        body.controls = [database_view]
        body.update()

    appbar = ft.AppBar(
        leading=ft.Image(
            src=f"images/cut.png",
            width=120,
            height=110,

        ),
        leading_width=40,
        title=ft.Text("LoDaLo - Login Data Lord", font_family='Freestyle Script', color='#b50938', size=45),
        center_title=True,
        bgcolor='#d6bac2',
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Classic Password Generator", on_click=passgen),
                    ft.PopupMenuItem(text="Login Generator", on_click=loggen),
                    ft.PopupMenuItem(text="Database Manager", on_click=database),
                    ft.Divider(height=9, thickness=3),
                    ft.PopupMenuItem(text="Refresh database", on_click=refresh)
                ],
            ),
        ],
    )
    body_con1 = ft.Text("Welcome! It's Your Login Data Lord!", font_family='Freestyle Script', color='#b50938', size=30)
    body = ft.Column([body_con1], alignment=ft.MainAxisAlignment.CENTER, expand=True)
    page.body = body
    page.add(appbar, body)


ft.app(target=main)