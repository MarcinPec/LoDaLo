import flet as ft
from flet import UserControl, Text, Row, Column, ElevatedButton, TextField, Divider
import l6_utility
import os


class OptionsMenu(UserControl):
    def __init__(self):
        super().__init__()
        self.pass_file = 'pass.txt'
        self.reg_cell_style = ft.TextStyle(font_family='Aptos', color='#00CCFF', size=18)
        self.dialog_title_style = ft.TextStyle(font_family='Freestyle Script', color='#00CCFF', size=35,
                                          weight=ft.FontWeight.BOLD)
        self.title = Text(value='Settings', size=100, color='#00CCFF', font_family='Freestyle Script')
        self.title_part1 = Text(value='Time period for auto-refresh mode (1-60s)', size=21, color='#00CCFF', font_family='Aptos')
        self.tf_part1 = TextField(label='max: 60s', border_color='#00CCFF',text_style=self.reg_cell_style)
        self.title_part2 = Text(value='Define new password to LoDaLo', size=21, color='#00CCFF', font_family='Aptos')
        self.button_part2 = ElevatedButton('Define!', animate_size=50, color='#00CCFF', on_click=self.show_def_dlg)
        self.loginfield = ft.TextField(password=True, can_reveal_password=True, border_color='#00CCFF')
        self.define_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Establish your password: ", style=self.dialog_title_style),
            content=self.loginfield,
            actions=[
                ft.ElevatedButton("Establish!", on_click=self.def_dlg, color='#00CCFF'),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
            on_dismiss=lambda e: print("Password established!"),
        )
        self.divider = Divider(color='#00CCFF', thickness=0.5, leading_indent=1)

    def show_def_dlg(self, e):
        self.define_dlg.open = True
        self.update()

    def def_dlg(self, e):
        if os.path.exists(self.pass_file):
            os.remove(self.pass_file)

        password_value = self.loginfield.value

        with open(self.pass_file, 'w') as passw:
            passw.write(password_value)

        print(l6_utility.EncryptTXT(self.pass_file))

        self.define_dlg.open = False
        self.update()

    def textfield_value_gen(self):
        try:
            value = int(self.tf_part1.value)
            if 1 <= value <= 60:
                return value
            else:
                print("Value out of range (1-60).")
                return 30  # Default value
        except ValueError:
            print("Invalid input, not an integer.")
            return 30  # Default value

    def build(self):
        row1 = Row([self.title])
        row2 = Row([self.title_part1, self.tf_part1])
        row3 = Row([self.title_part2, self.button_part2])
        row4 = Row([self.define_dlg])
        return Column(controls=[row1, row2, self.divider, row3, self.divider, row4], alignment=ft.MainAxisAlignment.START, scroll=ft.ScrollMode.ALWAYS)
