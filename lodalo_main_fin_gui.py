import flet as ft
import os.path
import asyncio
import passgener_app_gui, logingener_app_gui, database_app_gui, assocgener_app_gui, utility


def main(page: ft.Page):
    page.title = 'LoDaLo - Login Data Lord'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'light'
    body_con1 = ft.Image(
            src=f"images/lodalo_logo_v1.png",
            width=400,
            height=180,
        )
    body_con2 = ft.Text("Welcome in Phase0_v0.5!", font_family='Freestyle Script', color='#b50938', size=30)
    body_all = ft.Column(controls=[body_con1, body_con2])

    body_view = ft.Container(body_all, expand=True)
    classic_passgen_view = ft.Container(passgener_app_gui.PassGener(), expand=True)
    assoc_passgen_view = ft.Container(assocgener_app_gui.AssocPassGener(), expand=True)
    loggen_view = ft.Container(logingener_app_gui.LogGener(), expand=True)
    database_view = ft.Container(database_app_gui.DataBaseViewer(), expand=True)
    seconds_textfield = ft.TextField(label='time period', text_size=10, suffix_text='seconds', value='10')
    period = int(seconds_textfield.value)

    def refresh(_):
        body.controls = [body_view]
        body.update()
        body.controls = [database_view]
        body.update()

    async def auto_refresh(_):
        for _ in range(period):
            body.controls = [body_view]
            body.update()
            body.controls = [database_view]
            body.update()
            await asyncio.sleep(1)

    def home(_):
        body.controls = [body_view]
        body.update()

    def passgen(_):
        body.controls = [classic_passgen_view]
        body.update()

    def assoc_passgen(_):
        body.controls = [assoc_passgen_view]
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
        center_title=True,
        bgcolor='#d6bac2',
        actions=[
            ft.IconButton(
                icon=ft.icons.PLAY_ARROW,
                icon_color='#b50938',
                icon_size=35,
                tooltip="Auto-refresh database for time period",
                on_click=auto_refresh
            ),
            seconds_textfield,
            ft.IconButton(
                icon=ft.icons.REFRESH,
                icon_color='#b50938',
                icon_size=35,
                tooltip="Refresh database",
                on_click=refresh
            ),
            ft.IconButton(
                icon=ft.icons.HOME,
                icon_color='#b50938',
                icon_size=35,
                tooltip="Home",
                on_click=home
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Classic Password Generator", on_click=passgen),
                    ft.PopupMenuItem(text="Associational Password Generator", on_click=assoc_passgen),
                    ft.PopupMenuItem(text="Login Generator", on_click=loggen),
                    ft.PopupMenuItem(text="Database Manager", on_click=database),
                ],
                icon_color='#b50938',
                icon_size=35
            ),
        ],
    )
    loginfield = ft.TextField(password=True, can_reveal_password=True)
    welcometext = ft.Text('How are you today?')
    pass_file = 'pass.txt'

    def login_dlg(e):
        usual_dlg.open = True
        page.update()
        a = loginfield.value
        with open(pass_file, 'r') as passw:
            b = passw.read()

        if a == b:
            usual_dlg.open = False
            page.update()
        else:
            usual_dlg.open = True
            page.update()

    def ops_dlg(e):
        oops_dlg.open = True
        page.update()
        a = loginfield.value

        with open(pass_file, 'w') as passw:
            b = passw.write(a)

        oops_dlg.open = False
        page.update()
        usual_dlg.open = True
        page.update()

    def hello_dlg(e):
        if os.path.exists(pass_file):
            usual_dlg.open = True
            page.update()
        else:
            oops_dlg.open = True
            page.update()

    usual_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Enter the password: "),
        content=loginfield,
        actions=[
            ft.OutlinedButton("Login!", on_click=login_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Password correct!"),
    )

    oops_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Establish your password: "),
        content=loginfield,
        actions=[
            ft.OutlinedButton("Establish!", on_click=ops_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Password established!"),
    )
    welcome_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Welcome to LoDaLo!!!"),
        content=welcometext,
        actions=[
            ft.OutlinedButton("Good!", on_click=hello_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Nice!"),
    )

    welcome_dlg.open = True
    page.update()

    body = ft.Column([body_con1, body_con2], alignment=ft.MainAxisAlignment.CENTER, expand=True)
    page.body = body
    page.add(welcome_dlg, usual_dlg, oops_dlg, appbar, body)


ft.app(target=main)
