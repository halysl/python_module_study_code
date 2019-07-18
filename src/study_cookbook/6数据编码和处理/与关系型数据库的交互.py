# -* - coding: utf-8 -*-
import os
import sqlite3

path = os.path.dirname(__file__)


def example_interaction_sqlite():
    db = sqlite3.connect(os.path.join(path, "test.db"))
    c = db.cursor()
    c.execute('create table test (message text, id integer, price real)')
    db.commit()
    c.executemany('insert into test values (?,?,?)',
                  (('hello', 2, 1.0), ('world', 3, 2.1)))
    db.commit()
    for row in db.execute('select * from test'):
        print(row)

if __name__ == "__main__":
    example_interaction_sqlite()
