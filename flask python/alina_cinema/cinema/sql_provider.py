import os
from string import Template


# file_path это путь blueprint, os.listdir последовательно читает, открываем, считываем, file - имя product, создаем словарь
# в котором ключ - имя файла
class SQLProvider:
    def __init__(self, file_path: str):  # одержит путь файл к sql-запросам
        self._scripts = {}  # словарь
        for file in os.listdir(file_path):
            sql = open(f"{file_path}/{file}").read()  # для всех заготовок sql в директории filepath прочиать
            self._scripts[file] = Template(sql)

    def get(self, name, **kwargs):  # k - кол-во именованный параметров
        sql = self._scripts[name].substitute(**kwargs)  # подставляет шаблон sql-запроса
        return sql
