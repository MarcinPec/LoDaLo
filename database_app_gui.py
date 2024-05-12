import flet as ft
import datacsv_engine, utility
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row, DataTable, FilePickerResultEvent, FilePicker, OnScrollEvent


class DataFileSaver:
    def __init__(self, web, log, passw):
        self.web = web
        self.log = log
        self.passw = passw
        self.data_writer = datacsv_engine.DataLoginSaver(web, log, passw)

    def write_data(self):
        self.all_data_w = self.data_writer.file_maker()


class DataFileLoader:
    def __init__(self, filename):
        self.filename = filename
        self.data_reader = datacsv_engine.DataLoginReader(filename)
        self.all_data = self.data_reader.file_reader()

    def update_data(self):
        self.all_data = self.data_reader.file_reader()


class DataBaseViewer(UserControl):
    def __init__(self):
        super().__init__()
        self.textfield_www = ft.TextField(label='type WWW', text_size=15)
        self.textfield_log = ft.TextField(label='type Login', text_size=15)
        self.textfield_pass = ft.TextField(label='type Password', text_size=15, password=True, can_reveal_password=True)
        self.data_load = DataFileLoader('lodalo_database.csv')
        self.columns = [
            ft.DataColumn(label=ft.Text("WWW")),
            ft.DataColumn(label=ft.Text("Login")),
            ft.DataColumn(label=ft.Text("Password")),
            ft.DataColumn(label=ft.Text('Action')),
            ft.DataColumn(label=ft.Text(''))
        ]
        self.delete_but = ElevatedButton('Remove', color='#b50938')
        self.analyze_but = ElevatedButton('Analyze', color='#b50938')
        self.update_rows()

    def write_rows(self):
        self.data_write = DataFileSaver(self.textfield_www.value, self.textfield_log.value, self.textfield_pass.value)
        self.data_write.write_data()
        self.update_rows()

    def update_rows(self):
        self.data_load.update_data()
        self.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row['website'])),
                    ft.DataCell(ft.Text(row['login'])),
                    ft.DataCell(ft.Text(row['password'])),
                    ft.DataCell(self.delete_but),
                    ft.DataCell(self.analyze_but),
                ]
            ) for row in self.data_load.all_data
        ]

    def build(self):
        title = Text(value="Database Manager", size=100, color='#b50938', font_family='Freestyle Script')
        button_open = ElevatedButton('Open...', color='#b50938')
        button_add = ElevatedButton('Add to database', on_click=lambda event: self.write_rows(), color='#b50938')
        textfields_button = Row(controls=[
            self.textfield_www,
            self.textfield_log,
            self.textfield_pass,
            button_add,
            button_open])
        table = DataTable(
            columns=self.columns,
            rows=self.rows,
            width=1200
        )

        return Column(controls=[title, textfields_button, table], scroll=ft.ScrollMode.ALWAYS)



