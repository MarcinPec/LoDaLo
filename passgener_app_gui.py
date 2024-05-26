import flet as ft
import genpass_engine, ai_password_analizer_engine
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row


class PassGener(UserControl):
    def __init__(self):
        super().__init__()
        self.reg_cell_style = ft.TextStyle(font_family='Aptos', color='#00CCFF', size=18)
        self.c_numbs = ft.Checkbox(label='use numbers', value=False)
        self.c_letters = ft.Checkbox(label='use letters', value=False)
        self.c_special = ft.Checkbox(label='use special signs', value=False)
        self.textfield = ft.TextField(label='Password length - max: 25', border_color='#00CCFF',
                                      text_style=self.reg_cell_style)
        self.start_gen = genpass_engine.GenPass(10, self.c_numbs.value, self.c_letters.value,
                                                self.c_special.value)
        self.text_gen = ft.TextField(label='Generated password', value=str(self.start_gen), read_only=True,
                                     border_color='#00CCFF', text_style=self.reg_cell_style)
        self.title = Text(value="Classic Password Generator", size=100, color='#00CCFF', font_family='Freestyle Script')
        self.decription = Text(value='It generates hard to crack passwords in classic way', font_family='Aptos', size=15, color='#00CCFF')
        self.button = ElevatedButton('Generate!', on_click=self.generate, animate_size=50, color='#00CCFF')
        self.c1 = ft.Container(Row(controls=[self.strength_analizer(str(self.text_gen.value))]),
            alignment=ft.alignment.center,
            width=200,
            height=100
        )
        self.c2 = ft.Container(
            Row(controls=[self.strength_analizer(str(self.text_gen.value))]),
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
        self.error_dialog2 = ft.AlertDialog(
            modal=True,
            icon=ft.Icon(ft.icons.ERROR_SHARP, color='red'),
            title=ft.Text("Ooops!", style=dialog_title_style),
            content=self.dialog2text,
            actions=[
                ft.ElevatedButton("Ok", on_click=self.error_dlg2, color='#00CCFF'),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )

    def error_dlg(self, e):
        self.error_dialog.open = False
        self.error_dialog.update()

    def error_dlg2(self, e):
        self.error_dialog2.open = False
        self.error_dialog2.update()

    @staticmethod
    def strength_analizer(password):
        analize = ai_password_analizer_engine.PasswordStrengthModel(password)
        time_crack = analize.estimate_cracking_time()
        time2 = ai_password_analizer_engine.PasswordStrenghtTimer(password)
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
            self.start_gen = genpass_engine.GenPass(int(self.textfield.value), self.c_numbs.value, self.c_letters.value,
                                                    self.c_special.value)
            self.text_gen.value = str(self.start_gen)
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
        except genpass_engine.LengthError:
            self.error_dialog2.open = True
            self.error_dialog2.update()

    def build(self):
        title_row = Row(controls=[self.title, self.decription])
        check_field = Row(controls=[self.textfield, self.c_numbs, self.c_letters, self.c_special])
        row = Row(controls=[self.text_gen, self.button, self.c, self.error_dialog, self.error_dialog2])
        return Column(controls=[title_row, check_field, row], alignment=ft.MainAxisAlignment.START,
                      scroll=ft.ScrollMode.ALWAYS)
