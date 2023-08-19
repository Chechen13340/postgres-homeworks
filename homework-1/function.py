import csv


def get_data(path):
    """
    функция для получения данных из csv файлов
    """
    data_tables = []
    with open(path, 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            data_tables.append(row)
        return data_tables
