import csv


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
                writer.writeheader()
            writer.writerow({'website': self.website, 'login': self.login, 'password': self.password})

    def __str__(self):
        return f'{self.file_maker()}'


class DataLoginReader:
    def __init__(self, database):
        self.database = database

    def file_reader(self):
        with open(self.database, mode='r', newline='') as database:
            reader = csv.DictReader(database)
            for row in reader:
                print(row)

    def __str__(self):
        return f'{self.file_reader()}'


test_file = 'lodalo_database.csv'
test = DataLoginReader(test_file)
print(test)
