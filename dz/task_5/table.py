import psycopg2
import pandas as pd
import time
from datetime import datetime

class price_add:

    def __init__(self, conn, name, json_to_sql):
        self.dict_sql = {}
        self.conn = conn
        self.file_name = name
        self.json_to_sql = json_to_sql

    def refactor(self):
        for line in self.json_to_sql['data']:
            arr_data = []
            for price in line['price_change']:
                arr_data.append({'id': int(line['id']),
                                 'price': price['price'],
                                 'eff_from': price['eff_from']})
            self.dict_sql['id' + str(line['id'])] = arr_data

    def write_to_db(self, time1):
        with open('sql\\sql_1.sql','r') as f:
            sql_1 = f.read()
        with open('sql\\get_eff_to.sql','r') as f:
            sql_2 = f.read()
        with open('sql\\insert_to_process_journal.sql','r') as f:
            sql_3 = f.read()
        curs = self.conn.cursor()
        for i in self.dict_sql.values():
            for j in i:
                data = (
                    j['id'],
                    j['price'],
                    j['eff_from']
                )
                curs.execute(sql_1, data)
        curs.execute(sql_2)
        a = curs.fetchall()
        datetime1 = datetime.fromtimestamp(time1)
        datetime1 = datetime1.replace(microsecond=0)
        formatted_datetime1 = datetime1.strftime("%Y-%m-%d %H:%M:%S")
        datetime2 = datetime.fromtimestamp(time.time())
        datetime2 = datetime2.replace(microsecond=0)
        formatted_datetime2 = datetime2.strftime("%Y-%m-%d %H:%M:%S")
        print(datetime1)
        data_journal = (
            self.json_to_sql['process_id'],
            self.file_name,
            str(formatted_datetime1),
            str(formatted_datetime2)
        )
        curs.execute(sql_3, data_journal)
        self.conn.commit()

        return a

    def result(self,result):
        res = pd.DataFrame(result)
        del res[0]
        res = res.rename(columns={1: 'price', 2: 'eff_from', 3: 'id', 4: 'eff_to'})
        print(res)
        self.conn.close()