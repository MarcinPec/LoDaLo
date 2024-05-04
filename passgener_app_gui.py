import flet as ft
import genpass_engine
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row, TextField


class PassGener(UserControl):
    def __init__(self):
        super().__init__()
        self.c_numbs = ft.Checkbox(label='use numbers', value=False)
        self.c_letters = ft.Checkbox(label='use letters', value=False)
        self.c_special = ft.Checkbox(label='use special signs', value=False)
        self.textfield = ft.TextField(label='Password length - max: 75')
        self.start_gen = genpass_engine.GenPass(10, self.c_numbs.value, self.c_letters.value,
                                                self.c_special.value)
        self.text_gen = ft.TextField(label='Generated password', value=str(self.start_gen))

    def generate(self, e: ControlEvent):
        self.start_gen = genpass_engine.GenPass(int(self.textfield.value), self.c_numbs.value, self.c_letters.value,
                                                self.c_special.value)
        self.text_gen.value = str(self.start_gen)
        self.update()

    def build(self):
        title = Text(value="Password Generator", size=100, color='#b50938', font_family='Freestyle Script')
        check_field = Row(controls=[self.textfield, self.c_numbs, self.c_letters, self.c_special])
        button = ElevatedButton('Generate!', on_click=self.generate, animate_size=50, color='#b50938')
        row = self.text_gen
        return Column(controls=[title, check_field, row, button], alignment=ft.MainAxisAlignment.CENTER)