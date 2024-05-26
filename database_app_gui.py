import flet as ft
import datacsv_engine, utility, ai_password_analizer_engine
import csv
import webbrowser
from flet import Text, UserControl, ElevatedButton, Column, Row, DataTable


class DataFileSaver:
    def __init__(self, idn, web, log, passw):
        self.web = web
        self.log = log
        self.passw = passw
        self.idn = idn
        self.data_writer = datacsv_engine.DataLoginSaver(idn, web, log, passw)

    def write_data(self):
        self.all_data_w = self.data_writer.file_maker()


class DataFileLoader:
    def __init__(self, filename):
        self.filename = filename
        self.data_reader = datacsv_engine.DataLoginReader(filename)
        self.all_data = self.data_reader.file_reader()

    def update_data(self):
        self.all_data = self.data_reader.file_reader()


class DataFileOneRowLoader:
    def __init__(self, idg, filename):
        self.idg = idg
        self.filename = filename
        self.one_row_reader = datacsv_engine.DataLoginOneRowLoader(idg, filename)
        self.all_data = self.one_row_reader.one_row_reader()

    def one_row_update(self):
        self.all_data = self.one_row_reader.one_row_reader()


class DataFileOneRowSaver:
    def __init__(self, row_id, database, new_data):
        self.row_id = row_id
        self.database = database
        self.new_data = new_data
        self.one_row_saver = datacsv_engine.DataLoginOneRowSaver(row_id, database, new_data)
        self.all_data = self.one_row_saver.one_row_saver()

    def one_row_save(self):
        self.all_data = self.one_row_saver.one_row_saver()


class DataFileRemover:
    def __init__(self, idg, filename):
        self.idg = idg
        self.filename = filename
        self.data_remover = datacsv_engine.DataLoginRemover(idg, filename)
        self.all_data = self.data_remover.remover()

    def remove_data(self):
        self.all_data = self.data_remover.remover()


class DataBaseViewer(UserControl):
    def __init__(self):
        super().__init__()
        self.title_cell_style = ft.TextStyle(font_family='Freestyle Script', color='#00CCFF', size=30, letter_spacing=9)
        self.reg_cell_style = ft.TextStyle(font_family='Aptos', color='#00CCFF', size=18)
        self.textfield_www = ft.TextField(label='type WWW', text_size=15, text_style=self.reg_cell_style,
                                          border_color='#00CCFF')
        self.textfield_log = ft.TextField(label='type Login', text_size=15, text_style=self.reg_cell_style,
                                          border_color='#00CCFF')
        self.textfield_pass = ft.TextField(label='type Password', text_size=15, password=True, can_reveal_password=True,
                                           text_style=self.reg_cell_style, border_color='#00CCFF')
        self.textfield_edit_id = ft.TextField(label='type ID to edit', text_size=15, text_style=self.reg_cell_style,
                                              border_color='#00CCFF')
        self.textfield_edit = ft.TextField(label='Row to edit', text_size=15, text_style=self.reg_cell_style,
                                           border_color='#00CCFF')

        self.directory = 'lodalo_database.csv'
        self.data_load = DataFileLoader(self.directory)
        self.columns = [
            ft.DataColumn(label=ft.Text("ID", style=self.title_cell_style), numeric=True),
            ft.DataColumn(label=ft.Text("WWW", style=self.title_cell_style)),
            ft.DataColumn(label=ft.Text("Login", style=self.title_cell_style)),
            ft.DataColumn(label=ft.Text("Password", style=self.title_cell_style)),
            ft.DataColumn(label=ft.Text("Actions", style=self.title_cell_style)),
            ft.DataColumn(label=ft.Text("Strength", style=self.title_cell_style)),
            ft.DataColumn(label=ft.Text("Crack in: ", style=self.title_cell_style)),
        ]
        self.edit_but = ElevatedButton('Edit', color='#00CCFF', on_click=self.edit_row)
        self.save_but = ElevatedButton('Save row', color='#00CCFF', on_click=self.save_edited_row)
        self.update_rows()
        self.rowfield = ft.TextField(label='Edit row: ', text_size=15, hint_text='', border_color='#00CCFF')
        self.title = Text(value="Database Manager", size=100, color='#00CCFF', font_family='Freestyle Script')
        self.button_add = ElevatedButton('Add to database', on_click=lambda event: self.write_rows(), color='#00CCFF')
    def edit_row(self, e):
        row_to_edit = self.textfield_edit_id.value
        self.one_row_load = datacsv_engine.DataLoginOneRowLoader(row_to_edit, self.directory)
        self.textfield_edit.value = self.one_row_load

    def save_edited_row(self, e):
        row_to_edit = self.textfield_edit_id.value
        new_data = self.textfield_edit.value
        new_data_parts = new_data.split(',')
        new_data_dict = {'id': row_to_edit, 'website': new_data_parts[1], 'login': new_data_parts[2], 'password': new_data_parts[3]}
        self.one_row_saver = DataFileOneRowSaver(row_to_edit, self.directory, new_data_dict)
        self.one_row_saver.one_row_save()
        self.update_rows()
        print(new_data, new_data_parts)

    def remove_rows(self, row_to_remove):
        self.data_remove = DataFileRemover(row_to_remove, self.directory)
        self.data_remove.remove_data()
        self.update_rows()

    def id_counter(self):
        row_count = 0
        with open(self.directory, mode='r', newline='') as file:
            columnnames = ['id', 'website', 'login', 'password']
            reader = csv.DictReader(file, fieldnames=columnnames)
            for row in reader:
                row_count += 1
            return row_count

    def write_rows(self):
        self.data_write = DataFileSaver(self.id_counter(), self.textfield_www.value, self.textfield_log.value,
                                        self.textfield_pass.value)
        self.data_write.write_data()
        self.update_rows()
        self.update()

    @staticmethod
    def strength_analizer(password):
        analize = ai_password_analizer_engine.PasswordStrengthModel(password)
        time_crack = analize.estimate_cracking_time()
        if time_crack > 311040000000: #10 000 years
            return ft.Image(src=f"images/6.png", width=220, height=95)
        elif 311040000000 < time_crack > 3110400000:
            return ft.Image(src=f"images/5.png", width=220, height=95)
        elif 3110400000 < time_crack > 31104000:
            return ft.Image(src=f"images/4.png", width=220, height=95)
        elif 31104000 < time_crack > 259200:
            return ft.Image(src=f"images/3.png", width=220, height=95)
        elif 259200 < time_crack > 86400:
            return ft.Image(src=f"images/2.png", width=220, height=95)
        elif 86400 < time_crack > 60:
            return ft.Image(src=f"images/1.png", width=220, height=95)
        elif 60 < time_crack >= 0:
            return ft.Image(src=f"images/0.png", width=220, height=95)
        else:
            return ft.Text('Waiting to data...', color='black', font_family='Aptos', size=18, weight=ft.FontWeight.BOLD)

    @staticmethod
    def strength_time(password):
        inst = ai_password_analizer_engine.PasswordStrenghtTimer(password)
        obj = inst.timer_adjuster()
        return ft.Text(obj, color='black', font_family='Aptos', weight=ft.FontWeight.BOLD, size=18)

    def open_web_browser(self, url):
        webbrowser.open_new_tab(url)

    def update_rows(self):
        self.data_load.update_data()
        self.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row['id'], style=self.reg_cell_style)),
                    ft.DataCell(ft.TextField(row['website'],
                                             text_style=self.reg_cell_style,
                                             border=ft.InputBorder.NONE, read_only=True)),
                    ft.DataCell(ft.TextField(row['login'],
                                             text_style=self.reg_cell_style,
                                             border=ft.InputBorder.NONE, read_only=True)),
                    ft.DataCell(ft.TextField(row['password'],
                                             password=True,
                                             can_reveal_password=True,
                                             read_only=True,
                                             border=ft.InputBorder.NONE,
                                             text_style=self.reg_cell_style)),
                    ft.DataCell(Row([ft.IconButton(
                        icon=ft.icons.DELETE,
                        icon_color='#00CCFF',
                        tooltip='Delete record',
                        on_click=lambda e, row_to_remove=row['id']: self.remove_rows(row_to_remove)),
                        ft.IconButton(
                            icon=ft.icons.OPEN_IN_BROWSER,
                            icon_color='#00CCFF',
                            tooltip='Open in browser...',
                            on_click=lambda e, url=row['website']: self.open_web_browser(url)),
                    ])),
                    ft.DataCell(self.strength_analizer(row['password'])),
                    ft.DataCell(self.strength_time(row['password']))

                ]
            ) for row in self.data_load.all_data
        ]
        self.id_counter()

    def build(self):
        textfields_button = Row(controls=[
            self.textfield_www,
            self.textfield_log,
            self.textfield_pass,
            self.button_add])
        table = DataTable(
            columns=self.columns,
            rows=self.rows,
            width=1200,
            vertical_lines=ft.border.BorderSide(1, "#00CCFF"),
        )
        action_buttons = Row(controls=[self.textfield_edit_id, self.edit_but])
        action_buttons2 = Row(controls=[self.textfield_edit, self.save_but])

        return Column(controls=[self.title, textfields_button, action_buttons, action_buttons2, table], scroll=ft.ScrollMode.ALWAYS)



