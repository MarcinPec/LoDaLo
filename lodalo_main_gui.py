import flet as ft
import passgener_app_gui, logingener_app_gui, database_app_gui
from flet import Text, ControlEvent, Column, VerticalDivider, CrossAxisAlignment, Row


def main(page: ft.Page):
    page.title = 'LoDaLo - Login Data Lord'
    page.horizontal_alignment = 'center'
    page.window_width = 1920
    page.window_height = 1080
    page.window_resizable = False
    page.theme_mode = 'light'
    text_style_nav = ft.TextStyle(color='#b50938', size=30, font_family='Freestyle Script')
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
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False,
                    ),
                ]
            ),
        ],
    )
    body_con1 = ft.Text("Welcome! It's Your Login Data Lord!", font_family='Freestyle Script', color='#b50938', size=30)
    body = Column([body_con1], alignment=ft.MainAxisAlignment.CENTER)
    page.body = body
    passgen_view = passgener_app_gui.PassGener()
    loggen_view = logingener_app_gui.LogGener()
    database_view = database_app_gui.DataBaseViewer()

    def destination_changer(e: ControlEvent):
        if navigation_rail.selected_index == 0:
            body.controls = [passgen_view]
        elif navigation_rail.selected_index == 1:
            body.controls = [loggen_view]
        elif navigation_rail.selected_index == 2:
            body.controls = [database_view]
        body.update()

    navigation_rail = ft.NavigationRail(selected_index=0,
                                        label_type=ft.NavigationRailLabelType.ALL,
                                        extended=True,
                                        height=700,
                                        min_width=100,
                                        min_extended_width=40,
                                        selected_label_text_style=text_style_nav,
                                        unselected_label_text_style=text_style_nav,
                                        indicator_color='#b50938',
                                        indicator_shape=ft.RoundedRectangleBorder(radius=5),
                                        group_alignment=-1,
                                        destinations=[ft.NavigationRailDestination(icon=ft.icons.PASSWORD,
                                                                                   label='Password Generator'),
                                                      ft.NavigationRailDestination(icon=ft.icons.LOGIN,
                                                                                   label='Login Generator'),
                                                      ft.NavigationRailDestination(icon=ft.icons.DATASET,
                                                                                   label='Database Manager'),
                                                      ],
                                        #bgcolor='#d6bac2',
                                        on_change=destination_changer)
    second_row = ft.Row(controls=[navigation_rail, body], spacing=50, vertical_alignment=CrossAxisAlignment.START)
    page.add(appbar, second_row)


ft.app(main)
