from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Base, User, Role
import pytest


@pytest.fixture(scope='module', autouse=True)
def connect():
    print('conn...')
    conn_str = 'mysql+mysqlconnector://root:lightandwoqu@localhost:3306/pytest'
    engine = create_engine(conn_str, echo=True)
    db_session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = db_session()
    return session


@pytest.fixture(scope='function', autouse=True)
def start_test():
    print('\nstart test...')


def test_delete_data(connect):
    connect.query(User).delete()
    connect.query(Role).delete()
    assert connect.query(User).all() == []
    assert connect.query(Role).all() == []


def test_add_data(connect):
    u1 = User(name='Light', age=23)
    u2 = User(name='Ash', age=20)
    r = Role(name='user')
    connect.add(u1)
    connect.add(u2)
    connect.add(r)
    connect.commit()
    assert connect.query(User).all() != []
    assert connect.query(Role).all() != []


def test_select_data(connect):
    session = connect
    data1 = session.query(User).filter(User.id == '1').first()
    data2 = session.query(User).filter(User.id == '2').first()
    data3 = session.query(Role).filter(Role.id == '1').first()
    assert data1.name == 'Light' and data1.age == 23
    assert data2.name == 'Ash' and data2.age == 20
    assert data3.name == 'user'


def test_drop_table(connect):
    session = connect
    session.execute("drop table User")
    session.execute("drop table Role")
    assert session.execute('show tables').rowcount == 0
