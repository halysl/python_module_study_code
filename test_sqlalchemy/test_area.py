# -*- coding:utf-8 -*-

from sqlalchemy import create_engine, func
from sqlalchemy import desc
from sqlalchemy import distinct
from sqlalchemy.sql import exists
from sqlalchemy.sql.functions import random
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base


# DB_CONNECT_STRING = 'mysql+mysqlconnector://root:lightandwoqu@localhost:3306/test'
# engine = create_engine(DB_CONNECT_STRING, echo=True)
# Base = automap_base()
# Base.prepare()
# DB_Session = sessionmaker(bind=engine)
# session = DB_Session()


def get_database(host, db_name, user, password, port=3306):
    """
    create existed postgre database engine and get its table with sqlalchemy

    :param host:host name, eg:'192.168.8.8'
    :param db_name: postgre database's name,eg:'mydatabase'
    :param user: postgre database user's name, eg: 'myname'
    :param password: postgre databse user's password
    :return: db_engine, database engine,can used by sqlalchemy or pandas
             tables, database's tables
    """
    db_type = "mysql+mysqlconnector"  # postgresql+psycopg2
    string = "%s://%s:%s@%s:%s/%s" % (db_type, user, password, host, port, db_name)
    db_engine = create_engine(string, echo=False)
    # get sqlalchemy tables from database
    Base = automap_base()
    Base.prepare(db_engine, reflect=True)
    tables = Base.classes
    return db_engine, tables


db_engine, db_table = get_database(host='localhost', db_name='test', user='root', password='lightandwoqu')

session = sessionmaker(bind=db_engine)()

db_name = db_table.china_area
datas = session.query(db_name).filter(db_name.pid == 1046)
for data in datas:
    print(data.name)
session.close()
