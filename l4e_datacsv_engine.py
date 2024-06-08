from l6_utility import *


class DataLoginSaver:
    def __init__(self, idn: int, website: str, login: str, password: str):
        self.website = website
        self.login = login
        self.password = password
        self.idn = idn

    def file_maker(self):
        print(EncryptCSV('lodalo_database.csv'))
        with open('lodalo_database.csv', mode='a', newline='') as database:
            columnnames = ['id', 'website', 'login', 'password']
            writer = csv.DictWriter(database, fieldnames=columnnames)
            if database.tell() == 0:
                database.seek(0)
                writer.writeheader()
            writer.writerow({'id': self.idn, 'website': self.website, 'login': self.login, 'password': self.password})
        print(EncryptCSV('lodalo_database.csv'))

    def __str__(self):
        return f'{self.file_maker()}'


class DataLoginReader:
    def __init__(self, database, start_row=1):
        self.database = database
        self.start_row = start_row

    def file_reader(self):
        print(EncryptCSV(self.database))
        data = []
        id_iterator_fixer(self.database)
        with open(self.database, mode='r', newline='') as file:
            columnnames = ['id', 'website', 'login', 'password']
            reader = csv.DictReader(file, fieldnames=columnnames)
            for _ in range(self.start_row):
                next(reader)
            for row in reader:
                data.append(row)
        print(EncryptCSV(self.database))
        return data

    def __str__(self):
        return '\n'.join([str(row) for row in self.file_reader()])


class DataLoginOneRowLoader:
    def __init__(self, row_id, database):
        self.row_id = row_id
        self.database = database

    def one_row_reader(self):
        print(EncryptCSV(self.database))
        data = []
        with open(self.database, mode='r', newline='') as file:
            columnnames = ['id', 'website', 'login', 'password']
            reader = csv.DictReader(file, fieldnames=columnnames)
            for row in reader:
                if str(self.row_id) == row['id']:
                    data.append(row)
            print(EncryptCSV(self.database))
            return data

    def __str__(self):
        row_data = self.one_row_reader()
        return ','.join(row_data[0].values())


class DataLoginOneRowSaver:
    def __init__(self, row_id, database, new_data):
        self.row_id = row_id
        self.database = database
        self.new_data = new_data

    def one_row_saver(self):
        print(EncryptCSV(self.database))
        temp_data = []
        with open(self.database, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row['id'] == str(self.row_id):
                    for key, value in self.new_data.items():
                        if key in row:
                            row[key] = value
                temp_data.append(row)

        with open(self.database, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(temp_data)
        print(EncryptCSV(self.database))

    def __str__(self):
        return f'{self.one_row_saver()}'


class DataLoginRemover:
    def __init__(self, row_id, database):
        self.row_id = row_id
        self.database = database

    def remover(self):
        print(EncryptCSV(self.database))
        rows = []
        with open(self.database, mode='r', newline='') as database:
            reader = csv.DictReader(database)
            for row in reader:
                if str(self.row_id) != row['id']:
                    rows.append(row)

        with open(self.database, mode='w', newline='') as file:
            columnnames = ['id', 'website', 'login', 'password']
            writer = csv.DictWriter(file, fieldnames=columnnames)
            writer.writeheader()
            writer.writerows(rows)
        print(EncryptCSV(self.database))
        return rows

    def __str__(self):
        return '\n'.join([str(row) for row in self.remover()])

