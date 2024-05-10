import csv
from utility import *


class DataLoginSaver:
    def __init__(self, website: str, login: str, password: str):
        self.website = website
        self.login = login
        self.password = password

    def file_maker(self):
        with open('lodalo_database.csv', mode='a', newline='') as database:
            columnnames = ['website', 'login', 'password']
            writer = csv.DictWriter(database, fieldnames=columnnames)
            if database.tell() == 0:
                database.seek(0)
            writer.writerow({'website': self.website, 'login': self.login, 'password': self.password})

    def __str__(self):
        return f'{self.file_maker()}'


class DataLoginReader:
    def __init__(self, database):
        self.database = database

    def file_reader(self):
        data = []
        with open(self.database, mode='r', newline='') as file:
            columnnames = ['website', 'login', 'password']
            reader = csv.DictReader(file, fieldnames=columnnames)
            for row in reader:
                data.append(row)
            return data

    def __str__(self):
        return '\n'.join([str(row) for row in self.file_reader()])


test = DataLoginReader('lodalo_database.csv')
print(test)
