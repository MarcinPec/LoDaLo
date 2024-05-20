import flet as ft
import datacsv_engine, utility, ai_password_analizer_engine
import csv
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row, DataTable, FilePickerResultEvent


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
        self.textfield_www = ft.TextField(label='type WWW', text_size=15)
        self.textfield_log = ft.TextField(label='type Login', text_size=15)
        self.textfield_pass = ft.TextField(label='type Password', text_size=15, password=True, can_reveal_password=True)
        self.textfield_del = ft.TextField(label='type ID to remove', text_size=15)
        self.textfield_edit_id = ft.TextField(label='type ID to edit', text_size=15)
        self.textfield_edit = ft.TextField(label='Row to edit', text_size=15)

        self.directory = 'lodalo_database.csv'
        self.data_load = DataFileLoader(self.directory)
        self.columns = [
            ft.DataColumn(label=ft.Text("ID")),
            ft.DataColumn(label=ft.Text("WWW")),
            ft.DataColumn(label=ft.Text("Login")),
            ft.DataColumn(label=ft.Text("Password")),
            ft.DataColumn(label=ft.Text("Strength")),
        ]
        self.delete_but = ElevatedButton('Remove', color='#b50938', on_click=self.remove_rows)
        self.edit_but = ElevatedButton('Edit', color='#b50938', on_click=self.edit_row)
        self.save_but = ElevatedButton('Save row', color='#b50938', on_click=self.save_edited_row)
        self.update_rows()
        self.rowfield = ft.TextField(label='Edit row: ', text_size=15, hint_text='')
        self.edit_dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Edit row: "),
            content=self.rowfield,
            actions=[
                ft.OutlinedButton("Login!", on_click='')],
            actions_alignment=ft.MainAxisAlignment.CENTER)

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

    def remove_rows(self, e):
        row_to_remove = self.textfield_del.value
        self.data_remove = DataFileRemover(row_to_remove, self.directory)
        self.data_remove.remove_data()
        self.textfield_del.value = 'Removed!'
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

    def strength_analizer(self, password):
        analize = ai_password_analizer_engine.PasswordStrengthModel(password)
        time_crack = analize.estimate_cracking_time()
<<<<<<< HEAD
        if time_crack > 5184000000: #10 000 years
            return ft.Text('INCREDIBLY STRONG', color='#3aa832')
        else:
            return ft.Text('WORK IN PROGRESS', color='#f20707')
=======
        if time_crack > 311040000000: #10 000 years
            return ft.Text('INCREDIBLY STRONG', color='black', bgcolor='#0293fa')
        elif 311040000000 < time_crack > 3110400000:
            return ft.Text('VERY STRONG', color='black', bgcolor='#3aa832')
        elif 3110400000 < time_crack > 31104000:
            return ft.Text('STRONG', color='black', bgcolor='#76fa02')
        elif 31104000 < time_crack > 259200:
            return ft.Text('MEDIUM', color='black', bgcolor='#d1fa02')
        elif 259200 < time_crack > 86400:
            return ft.Text('WEAK', color='black', bgcolor='#fae902')
        elif 86400 < time_crack > 60:
            return ft.Text('VERY WEAK', color='black', bgcolor='#faac02')
        elif 60 < time_crack >= 0:
            return ft.Text('RIDICOLOUSLY WEAK!', color='black', bgcolor='#fa4902')
        else:
            return ft.Text('Waiting to data...', color='black')
>>>>>>> Experimental_ai

    def update_rows(self):
        self.data_load.update_data()
        self.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row['id'])),
                    ft.DataCell(ft.Text(row['website'])),
                    ft.DataCell(ft.Text(row['login'])),
                    ft.DataCell(ft.TextField(row['password'],
                                             password=True,
                                             can_reveal_password=True,
                                             read_only=True,
                                             border=ft.InputBorder.NONE)),
                    ft.DataCell(self.strength_analizer(row['password']))

                ]
            ) for row in self.data_load.all_data
        ]
        self.id_counter()

    def build(self):
        title = Text(value="Database Manager", size=100, color='#b50938', font_family='Freestyle Script')
        button_add = ElevatedButton('Add to database', on_click=lambda event: self.write_rows(), color='#b50938')
        textfields_button = Row(controls=[
            self.textfield_www,
            self.textfield_log,
            self.textfield_pass,
            button_add])
        table = DataTable(
            columns=self.columns,
            rows=self.rows,
            width=1200
        )
        action_buttons = Row(controls=[self.textfield_edit_id, self.edit_but, self.textfield_edit, self.save_but])
        action_buttons2 = Row(controls=[self.textfield_del, self.delete_but])

        return Column(controls=[title, textfields_button, action_buttons, action_buttons2, table], scroll=ft.ScrollMode.ALWAYS)



