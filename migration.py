import csv
import sqlite3

def migrate():
    with sqlite3.connect('utils/tables.db') as con:
        cursorObj = con.cursor()
        cursorObj.execute('create table if not exists Tables(id integer PRIMARY KEY, name text NOT NULL, amount integer)')

        with open('utils/Table.csv', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for index, row in enumerate(csv_reader):
                print(index, row)
                cursorObj.execute("insert or replace into Tables VALUES(?, ?, ?)", (index+1, row['Name'], row['Amount']))

        con.commit()

def get_sum(name):
    with sqlite3.connect('utils/tables.db') as con:
        cursorObj = con.cursor()
        cursorObj.execute('SELECT sum(amount) FROM Tables WHERE name = "{}"'.format(name))

        return cursorObj.fetchall()[0][0]

    return None

if __name__ == '__main__':
    migrate()