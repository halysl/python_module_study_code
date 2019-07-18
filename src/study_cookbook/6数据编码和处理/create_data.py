# -*- coding: utf-8 -*-

import os
import sqlite3

path = os.path.join(os.path.dirname(__file__), "test.db")


def init_db(cur):
    sql = "drop table test"
    cur.execute(sql)


def create_table(cur):
    sql = "create table test (id integer, message text)"
    cur.execute(sql)


def insert_date(cur):
    sql = "insert into test values (1, 'hello'),(2, 'world'),(3, '!')"
    cur.execute(sql)

if __name__ == "__main__":
    db = sqlite3.connect(path)
    c = db.cursor()
    init_db(c)
    create_table(c)
    db.commit()
    insert_date(c)
    db.commit()
