import flet as ft
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row
import assoc_bigram_genpass_engine


class AssocPassGener(UserControl):
    def __init__(self):
        super().__init__()
        self.title = Text(value="Associational Password Generator", size=100, color='#b50938', font_family='Freestyle Script')
        self.length = ft.TextField(label='Length')
        self.word1 = ft.TextField(label='First word')
        self.word2 = ft.TextField(label='Second word')
        self.c_separate = ft.Checkbox(label='Separate segments of password', value=False)
        self.c_polish = ft.Checkbox(label='Use polish dictionary', value=False)
        self.start_gen = assoc_bigram_genpass_engine.AsociationalBigramPassGen(10, 'auto', 'kupa',
                                                                               False, False)
        self.text_gen = ft.TextField(label='Generated password', value=str(self.start_gen), read_only=True)
        self.button_gen = ft.OutlinedButton('Generate!', on_click=self.generate, animate_size=50)

    def generate(self, e: ControlEvent):
        self.just_gen = assoc_bigram_genpass_engine.AsociationalBigramPassGen(int(self.length.value), self.word1.value,
                                                                              self.word2.value, self.c_separate.value,
                                                                              self.c_polish.value)
        self.text_gen.value = str(self.just_gen)
        self.update()

    def build(self):
        title_row = Row(controls=[self.title])
        text_field = Row(controls=[self.length, self.word1, self.word2])
        check_field = Row(controls=[self.c_separate, self.c_polish])
        result_field = Row(controls=[self.text_gen, self.button_gen])
        return Column(controls=[title_row, text_field, check_field, result_field],alignment=ft.MainAxisAlignment.START,
                      scroll=ft.ScrollMode.ALWAYS)




