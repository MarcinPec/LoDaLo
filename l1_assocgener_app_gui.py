import flet as ft
from flet import Text, UserControl, ControlEvent, Column, Row
import l1e_assoc_bigram_genpass_engine, l7_ai_password_analizer_engine


class AssocPassGener(UserControl):
    def __init__(self):
        super().__init__()
        self.reg_cell_style = ft.TextStyle(font_family='Aptos', color='#00CCFF', size=18)
        self.title = Text(value="Associational Password Generator", size=100, color='#00CCFF', font_family='Freestyle Script')
        self.decription = Text(
            value=f'This generator creates passwords using AI model',
            font_family='Aptos', size=15, color='#00CCFF')
        self.word1 = ft.TextField(label='First word', border_color='#00CCFF', text_style=self.reg_cell_style)
        self.word2 = ft.TextField(label='Second word', border_color='#00CCFF', text_style=self.reg_cell_style)
        self.c_separate = ft.Checkbox(label='Separate segments of password', value=False)
        self.c_polish = ft.Checkbox(label='Use polish dictionary', value=False)
        self.c_english = ft.Checkbox(label='Use english dictionary', value=False)
        self.start_gen = l1e_assoc_bigram_genpass_engine.AsociationalBigramPassGen('auto', 'kupa',
                                                                               False, True, True)
        self.text_gen = ft.TextField(label='Generated password', value=str(self.start_gen), read_only=True,
                                     border_color='#00CCFF', text_style=self.reg_cell_style)
        self.button_gen = ft.ElevatedButton('Generate!', on_click=self.generate, animate_size=50, color='#00CCFF')
        self.c1 = ft.Container(
            self.strength_analizer(str(self.text_gen.value)),
            alignment=ft.alignment.center,
            width=200,
            height=100
        )
        self.c2 = ft.Container(
            self.strength_analizer(str(self.text_gen.value)),
            alignment=ft.alignment.center,
            width=200,
            height=100,
        )
        self.c = ft.AnimatedSwitcher(
            self.c1,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=500,
            reverse_duration=100,
            switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
            switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
        )
        dialog_text_style = ft.TextStyle(font_family='Aptos', color='#00CCFF', size=20)
        dialog_title_style = ft.TextStyle(font_family='Freestyle Script', color='#00CCFF', size=25,
                                          weight=ft.FontWeight.BOLD)
        self.dialogtext = ft.Text('Incorrect value!', style=dialog_text_style)
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

    @staticmethod
    def strength_analizer(password):
        analize = l7_ai_password_analizer_engine.PasswordStrengthModel(password)
        time_crack = analize.estimate_cracking_time()
        time2 = l7_ai_password_analizer_engine.PasswordStrenghtTimer(password)
        crackt = time2.timer_adjuster()
        if time_crack > 311040000000:  # 10 000 years
            return Row(controls=[ft.Image(src=f"images/6.png", width=220, height=95), ft.Text(crackt)])
        elif 311040000000 < time_crack > 3110400000:
            return Row(controls=[ft.Image(src=f"images/5.png", width=220, height=95), ft.Text(crackt)])
        elif 3110400000 < time_crack > 31104000:
            return Row(controls=[ft.Image(src=f"images/4.png", width=220, height=95), ft.Text(crackt)])
        elif 31104000 < time_crack > 259200:
            return Row(controls=[ft.Image(src=f"images/3.png", width=220, height=95), ft.Text(crackt)])
        elif 259200 < time_crack > 86400:
            return Row(controls=[ft.Image(src=f"images/2.png", width=220, height=95), ft.Text(crackt)])
        elif 86400 < time_crack > 60:
            return Row(controls=[ft.Image(src=f"images/1.png", width=220, height=95), ft.Text(crackt)])
        elif 60 < time_crack >= 0:
            return Row(controls=[ft.Image(src=f"images/0.png", width=220, height=95), ft.Text(crackt)])
        else:
            return ft.Text('Waiting to data...', color='black', font_family='Aptos', size=18, weight=ft.FontWeight.BOLD)

    def generate(self, e: ControlEvent):
        try:
            self.just_gen = l1e_assoc_bigram_genpass_engine.AsociationalBigramPassGen(self.word1.value,self.word2.value,
                                                                                  self.c_separate.value, self.c_polish.value,
                                                                                  self.c_english.value)
            self.text_gen.value = str(self.just_gen)
            new_strength = self.strength_analizer(self.text_gen.value)
            if self.c.content == self.c1:
                self.c2.content = new_strength
                self.c.content = self.c2
            else:
                self.c1.content = new_strength
                self.c.content = self.c1
            self.c.update()
            self.update()
        except ValueError:
            self.error_dialog.open = True
            self.error_dialog.update()

    def build(self):
        title_row = Row(controls=[self.title, self.decription])
        text_field = Row(controls=[self.word1, self.word2])
        check_field = Row(controls=[self.c_separate, self.c_polish, self.c_english])
        result_field = Row(controls=[self.text_gen, self.button_gen, self.c, self.error_dialog])
        return Column(controls=[title_row, text_field, check_field, result_field], alignment=ft.MainAxisAlignment.START,
                      scroll=ft.ScrollMode.ALWAYS)




