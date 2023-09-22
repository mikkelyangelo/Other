import json
import psycopg2
import os

def json_conf():
    with open ('json\\json_1.json','r') as json_file:
        json_to_sql = json.load(json_file)
    name = os.path.basename(r'json\\json_1.json')
    arr = (name,json_to_sql)
    return arr

def conn_conf():
    conn = psycopg2.connect(dbname="test2", user="postgres", password="123", host="localhost")
    return conn
