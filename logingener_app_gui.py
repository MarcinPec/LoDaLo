import flet as ft
import genlogin_engine
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row


class LogGener(UserControl):
    def __init__(self):
        super().__init__()
        self.reg_cell_style = ft.TextStyle(font_family='Aptos', color='#00CCFF', size=18)
        self.title = Text(value="Login Generator", size=100, color='#00CCFF', font_family='Freestyle Script')
        self.decription = Text(
            value='It s simple generator that simply creates logins.',font_family='Aptos', size=15, color='#00CCFF')
        self.c_numbs = ft.Checkbox(label='use numbers', value=False)
        self.c_letters = ft.Checkbox(label='use letters', value=False)
        self.c_special = ft.Checkbox(label='use special signs', value=False)
        self.textfield = ft.TextField(label='Password length - max: 75', border_color='#00CCFF',
                                      text_style=self.reg_cell_style)
        self.lengthfield = ft.TextField(label='Login pattern', border_color='#00CCFF', text_style=self.reg_cell_style)
        self.start_gen = genlogin_engine.GenLog('test', 10, self.c_numbs.value, self.c_letters.value,
                                                self.c_special.value)
        self.text_gen = ft.TextField(label='Generated password', value=str(self.start_gen), read_only=True,
                                     border_color='#00CCFF', text_style=self.reg_cell_style)
        dialog_text_style = ft.TextStyle(font_family='Aptos', color='#00CCFF', size=20)
        dialog_title_style = ft.TextStyle(font_family='Freestyle Script', color='#00CCFF', size=25,
                                          weight=ft.FontWeight.BOLD)
        self.dialogtext = ft.Text('Incorrect value!', style=dialog_text_style)
        self.dialog2text = ft.Text('To long to generate!', style=dialog_text_style)
        self.error_dialog = ft.AlertDialog(
            modal=True,
            icon=ft.Icon(ft.icons.ERROR_SHARP, color='red'),
            title=ft.Text("Ooops!", style=dialog_title_style),
            content=self.dialogtext,
            actions=[
                ft.ElevatedButton("Ok", on_click=self.error_dlg, color='#00CCFF'),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )

    def error_dlg(self, e):
        self.error_dialog.open = False
        self.error_dialog.update()

    def generate(self, e: ControlEvent):
        try:
            self.start_gen = genlogin_engine.GenLog(self.lengthfield.value, int(self.textfield.value), self.c_numbs.value,
                                                    self.c_letters.value, self.c_special.value)
            self.text_gen.value = str(self.start_gen)
            self.update()
        except ValueError:
            self.error_dialog.open = True
            self.error_dialog.update()

    def build(self):
        title_row = Row(controls=[self.title, self.decription])
        text_fields = Row(controls=[self.lengthfield, self.textfield])
        check_field = Row(controls=[self.c_numbs, self.c_letters, self.c_special])
        button = ElevatedButton('Generate!', on_click=self.generate, animate_size=50, color='#00CCFF')
        row = Row(controls=[self.text_gen, button, self.error_dialog])
        return Column(controls=[title_row, text_fields, check_field, row], alignment=ft.MainAxisAlignment.START,
                      scroll=ft.ScrollMode.ALWAYS)
