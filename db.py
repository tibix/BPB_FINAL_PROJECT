import sqlite3
from sqlite3 import Error
from time import sleep

def create_connection(db_file):
    """ Create a database connection to a SQLite Database located in  db/ folder """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        for l in f'Database exists. Version {sqlite3.version}':
            sleep(0.1)
            print(l, end=' ')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

