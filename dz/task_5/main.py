from configs import json_conf, conn_conf
from table import price_add
import time

conn = conn_conf()
json_to_sql = json_conf() #

def main():
    time1 = time.time() #время начала работы
    table_insert = price_add(conn, json_to_sql[0], json_to_sql[1]) #создание обьекта класса price_add
    table_insert.refactor() #запись данных json'а в словарь dict_sql
    result = table_insert.write_to_db(time1) #выполнение запросов
    table_insert.result(result) #вывод таблицы (задание п.3)

if __name__ == '__main__':
    main()
