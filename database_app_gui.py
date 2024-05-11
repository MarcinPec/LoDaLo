import flet as ft
import datacsv_engine, utility
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row, DataTable, FilePickerResultEvent, FilePicker


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
        self.textfield_www = ft.TextField(label='type WWW')
        self.textfield_log = ft.TextField(label='type Login')
        self.textfield_pass = ft.TextField(label='type Password')
        self.data_load = DataFileLoader('lodalo_database.csv')
        self.columns = [
            ft.DataColumn(label=ft.Text("WWW")),
            ft.DataColumn(label=ft.Text("Login")),
            ft.DataColumn(label=ft.Text("Password")),
        ]

        self.update_rows()

    def write_rows(self):
        self.data_write = DataFileSaver(self.textfield_www.value, self.textfield_log.value, self.textfield_pass.value)
        self.data_write.write_data()

    def update_rows(self):
        self.data_load.update_data()
        self.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row['website'])),
                    ft.DataCell(ft.Text(row['login'])),
                    ft.DataCell(ft.Text(row['password']))
                ]
            ) for row in self.data_load.all_data
        ]

    def update_event(self):
        self.update_rows()

    def build(self):
        button_open = ElevatedButton('Open...', disabled=True)
        button_add = ElevatedButton('Add to database', on_click=lambda event: self.write_rows())
        button_refresh = ElevatedButton('Refresh', on_click=lambda event: self.update_event())
        textfields_button = Row(controls=[self.textfield_www, self.textfield_log, self.textfield_pass, button_add, button_open])
        refresh_button = Row(controls=[button_refresh])
        table = DataTable(columns=self.columns, rows=self.rows)
        return Column(controls=[textfields_button, refresh_button, table])



