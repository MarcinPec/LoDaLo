import flet as ft
import datacsv_engine, utility
from flet import Text, UserControl, ControlEvent, ElevatedButton, Column, Row, DataTable


class DataBaseViewer(UserControl):
    def __init__(self):
        super().__init__()
        data_reader = datacsv_engine.DataLoginReader('lodalo_database.csv')
        all_data = data_reader.file_reader()
        self.textfield_www = ft.TextField(label='type WWW')
        self.textfield_log = ft.TextField(label='type Login')
        self.textfield_pass = ft.TextField(label='type Password')
        self.columns = [
            ft.DataColumn(label=ft.Text("WWW")),
            ft.DataColumn(label=ft.Text("Login")),
            ft.DataColumn(label=ft.Text("Password")),
        ]

        self.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row['website'])),
                    ft.DataCell(ft.Text(row['login'])),
                    ft.DataCell(ft.Text(row['password']))
                ]
            ) for row in all_data
        ]

    def build(self):
        textfields = Row(controls=[self.textfield_www, self.textfield_log, self.textfield_pass])
        table = DataTable(columns=self.columns, rows=self.rows)
        return Column(controls=[textfields, table])



