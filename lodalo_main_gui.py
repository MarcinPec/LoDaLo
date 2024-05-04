import sys

import flet as ft
import passgener_app_gui
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row, TextField, VerticalDivider


def main(page: ft.Page):
    page.title = 'LoDaLo - Login Data Lord'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_width = 1000
    page.window_height = 700
    page.window_resizable = False
    page.theme_mode = 'light'

    logo = ft.Image(
        src=f"images/lodalo_logo_v1.png",
        width=800,
        height=250,
        fit=ft.ImageFit.COVER,
    )
    text_logo = Text('Welcome in LoDaLo App!! (Phase 0)', font_family='FreeStyle Script', color='#b50938', size=60)

    main_view = Column([logo, VerticalDivider(width=1, color='red'), text_logo, ])
    feedback_text = Text(value='')
    password_gen_view = passgener_app_gui.PassGener()
    login_gen_view = Text('Here will be a login generator...')
    database_view = Text('Here will be a database manager...')

    def bar_destination_changer(e: ControlEvent):
        feedback_text.value = 'Loading...'
        main_view.update()
        if page.navigation_bar.selected_index == 0:
            main_view.controls = [password_gen_view]
            feedback_text.value = 'Password Generator'
        elif page.navigation_bar.selected_index == 1:
            main_view.controls = [login_gen_view]
            feedback_text.value = 'Login Generator'
        elif page.navigation_bar.selected_index == 1:
            main_view.controls = [database_view]
            feedback_text.value = 'Database Manager'
        main_view.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label='Password Generator'),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label='Login Generator'),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label='Database manager'),

        ],
        on_change=bar_destination_changer,
    )

    main_view.controls.append(feedback_text)
    page.add(main_view)


ft.app(main)

