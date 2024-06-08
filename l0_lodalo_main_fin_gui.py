import flet as ft
import os.path
import asyncio
import webbrowser
import l2_passgener_app_gui, l3_logingener_app_gui, l4_database_app_gui, l1_assocgener_app_gui, l5_settings_app, l6_utility


def main(page: ft.Page):
    page.title = 'LoDaLo - Login Data Lord'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'light'
    body_con1 = ft.Image(
            src=f"images/lodalo_logo.png",
            width=400,
            height=180,
        )
    body_con2 = ft.Text("Welcome in Final_v0.8!", font_family='Aptos', color='#00CCFF', size=18)
    body_all = ft.Column(controls=[body_con1, body_con2])

    body_view = ft.Container(body_all, expand=True)
    classic_passgen_view = ft.Container(l2_passgener_app_gui.PassGener(), expand=True)
    assoc_passgen_view = ft.Container(l1_assocgener_app_gui.AssocPassGener(), expand=True)
    loggen_view = ft.Container(l3_logingener_app_gui.LogGener(), expand=True)
    database_view = ft.Container(l4_database_app_gui.DataBaseViewer(), expand=True)
    settings_view = ft.Container(l5_settings_app.OptionsMenu(), expand=True)
    period_raw = l5_settings_app.OptionsMenu()
    dialog_text_style = ft.TextStyle(font_family='Aptos', color='#00CCFF', size=19)
    dialog_title_style = ft.TextStyle(font_family='Freestyle Script', color='#00CCFF', size=35, weight=ft.FontWeight.BOLD)

    def refresh(_):
        body.controls = [body_view]
        body.update()
        body.controls = [database_view]
        body.update()

    async def auto_refresh(_):
        period = int(period_raw.textfield_value_gen())
        for _ in range(period):
            body.controls = [body_view]
            body.update()
            body.controls = [database_view]
            body.update()
            await asyncio.sleep(1)

    def home(_):
        body.controls = [body_view]
        body.update()

    def settings(_):
        body.controls = [settings_view]
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

    def author_dlg_open(e):
        author_dlg.open = True
        page.update()

    def author_dlg_close(e):
        author_dlg.open = False
        page.update()

    def open_web_browser(url):
        webbrowser.open_new_tab(url)

    appbar = ft.AppBar(
        leading=ft.Image(
            src=f"images/lodalo_cut.png",
            width=120,
            height=110,

        ),
        title=ft.Text('Login Data Lord - v0.8', font_family='Freestyle Script', size=45, color='#00CCFF'),
        leading_width=40,
        center_title=True,
        bgcolor='#cae0e6',
        actions=[
            ft.IconButton(
                icon=ft.icons.PLAY_ARROW,
                icon_color='#00CCFF',
                icon_size=35,
                tooltip="Auto-refresh database for time period",
                on_click=auto_refresh
            ),
            ft.IconButton(
                icon=ft.icons.REFRESH,
                icon_color='#00CCFF',
                icon_size=35,
                tooltip="Refresh database",
                on_click=refresh
            ),
            ft.IconButton(
                icon=ft.icons.HOME,
                icon_color='#00CCFF',
                icon_size=35,
                tooltip="Home",
                on_click=home
            ),
            ft.IconButton(
                icon=ft.icons.SETTINGS_SUGGEST,
                icon_color='#00CCFF',
                icon_size=35,
                tooltip="Settings",
                on_click=settings
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Classic Password Generator", on_click=passgen),
                    ft.PopupMenuItem(text="Associational Password Generator", on_click=assoc_passgen),
                    ft.PopupMenuItem(text="Login Generator", on_click=loggen),
                    ft.PopupMenuItem(text="Database Manager", on_click=database),
                    ft.Divider(),
                    ft.PopupMenuItem(text="About author...", on_click=author_dlg_open)
                ],
                icon_color='#00CCFF',
                icon_size=35
            ),
        ],
    )
    loginfield = ft.TextField(password=True, can_reveal_password=True, border_color='#00CCFF')
    welcometext = ft.Text('How are you today?', style=dialog_text_style)
    author_note1 = ft.Text('This app is created by Marcin Pecuch, 52763', style=dialog_text_style)
    author_note2 = ft.OutlinedButton('GitHub',
                                     on_click=lambda e, url='https://github.com/MarcinPec': open_web_browser(url))
    author_all = ft.Row([author_note1, author_note2])
    pass_file = 'pass.txt'

    def login_dlg(e):
        usual_dlg.open = True
        page.update()
        a = loginfield.value
        print(l6_utility.EncryptTXT(pass_file))
        with open(pass_file, 'r') as passw:
            b = passw.read()

        if a == b:
            usual_dlg.open = False
            page.update()
            print(l6_utility.EncryptTXT(pass_file))
        else:
            usual_dlg.open = True
            page.update()

    def ops_dlg(e):
        oops_dlg.open = True
        page.update()
        a = loginfield.value

        with open(pass_file, 'w') as passw:
            passw.write(a)

        oops_dlg.open = False
        page.update()
        print(l6_utility.EncryptTXT(pass_file))
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
        title=ft.Text("Password: ", style=dialog_title_style),
        content=loginfield,
        actions=[
            ft.ElevatedButton("Login!", on_click=login_dlg, color='#00CCFF'),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Password correct!"),
    )

    oops_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Establish your password: ", style=dialog_title_style),
        content=loginfield,
        actions=[
            ft.ElevatedButton("Establish!", on_click=ops_dlg, color='#00CCFF'),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Password established!"),
    )
    welcome_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("Welcome to LoDaLo!!!", style=dialog_title_style),
        content=welcometext,
        actions=[
            ft.ElevatedButton("Good!", on_click=hello_dlg, color='#00CCFF'),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Nice!"),
    )

    author_dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("About author...", style=dialog_title_style),
        content=author_all,
        actions=[
            ft.ElevatedButton("Close!", on_click=author_dlg_close, color='#00CCFF'),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    welcome_dlg.open = True
    page.update()

    body = ft.Column([body_con1, body_con2], alignment=ft.MainAxisAlignment.CENTER, expand=True)
    page.body = body
    page.add(welcome_dlg, usual_dlg, oops_dlg, appbar, body, author_dlg)


ft.app(target=main)
