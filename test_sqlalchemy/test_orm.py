#!/usr/bin/env python
#  -*-coding:utf-8-*-

# 导入:
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Base, User, Role

CONN_STR = 'mysql+mysqlconnector://root:lightandwoqu@localhost:3306/test'

class TEST_ORM(object):
    """sqlalchemy学习"""
    def __init__(self, conn_str, echo=True):
        self.CONN_STR = conn_str
        # 创建一个连接器
        self.engine = create_engine(self.CONN_STR, echo=echo)
        # 创建一个数据库连接
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def create_table(self):
        # MetaData是一个注册表，包括向数据库发出一组有限的模式生成命令的功能
        # 由于我们的MySQL数据库实际上没有用户表，我们可以使用MetaData为所有尚不存在的表向数据库发出CREATE TABLE语句
        # 下面，我们调用MetaData.create_all()方法
        # 将我们的Engine作为数据库连接源传递
        # 我们将看到首先发出特殊命令以检查user表是否存在，然后是实际的CREATE TABLE语句
        Base.metadata.create_all(self.engine)
        # 2018-08-28 15:59:35,144 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
        # 2018-08-28 15:59:35,144 INFO sqlalchemy.engine.base.Engine {}
        # 2018-08-28 15:59:35,146 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
        # 2018-08-28 15:59:35,146 INFO sqlalchemy.engine.base.Engine {}
        # 2018-08-28 15:59:35,147 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
        # 2018-08-28 15:59:35,147 INFO sqlalchemy.engine.base.Engine {}
        # 2018-08-28 15:59:35,147 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
        # 2018-08-28 15:59:35,147 INFO sqlalchemy.engine.base.Engine {}
        # 2018-08-28 15:59:35,148 INFO sqlalchemy.engine.base.Engine DESCRIBE `User`
        # 2018-08-28 15:59:35,148 INFO sqlalchemy.engine.base.Engine {}
        # 2018-08-28 15:59:35,148 INFO sqlalchemy.engine.base.Engine ROLLBACK
        # 2018-08-28 15:59:35,149 INFO sqlalchemy.engine.base.Engine
        # CREATE TABLE `User` (
        # 	id INTEGER NOT NULL AUTO_INCREMENT,
        # 	name VARCHAR(50),
        # 	age INTEGER,
        # 	PRIMARY KEY (id)
        # )
        #
        #
        # 2018-08-28 15:59:35,149 INFO sqlalchemy.engine.base.Engine {}
        # 2018-08-28 15:59:35,360 INFO sqlalchemy.engine.base.Engine COMMIT

    def add(self, data):
        """添加数据"""
        self.session.add(data)

    def commit(self):
        """提交数据"""
        self.session.commit()

    def select_all(self, table_name):
        """选择表中全部数据"""
        return self.session.query(table_name).all()

    def merge(self, data):
        """修改数据，若数据存在则修改，不存在则创建"""
        self.session.merge(data)

    def filter_update(self):
        self.session.query(User).filter(User.id == 1).update({'age': 40})

    def close(self):
        """关闭连接"""
        self.session.close()


t = TEST_ORM(CONN_STR)
t.create_table()

t.filter_update()

user = t.select_all(User)
print(user)

t.close()

# session.add(u)
# session.add(r)
# session.commit()
# 关闭session:
# role = session.query(User).all()
# session.close()
#
# print(role)


DB_CONNECT_STRING = 'sqlite:////Users/zhengxiankai/Desktop/Document/db.sqlite'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

# 1. 创建表（如果表已经存在，则不会创建）
Base.metadata.create_all(engine)

# 2. 插入数据
u = User(name = 'tobi', age = 200)
r = Role(name = 'user')

# 2.1 使用add，如果已经存在，会报错
session.add(u)
session.add(r)
session.commit()
print r.id

# 3 修改数据
# 3.1 使用merge方法，如果存在则修改，如果不存在则插入（只判断主键，不判断unique列）
r.name = 'admin'
session.merge(r)

# 3.2 也可以通过这种方式修改
session.query(Role).filter(Role.id == 1).update({'name': 'admin'})

# 4. 删除数据
session.query(Role).filter(Role.id == 1).delete()

# 5. 查询数据
# 5.1 返回结果集的第二项
user = session.query(User).get(2)

# 5.2 返回结果集中的第2-3项
users = session.query(User)[1:3]

# 5.3 查询条件
user = session.query(User).filter(User.id < 6).first()

# 5.4 排序
users = session.query(User).order_by(User.name)

# 5.5 降序（需要导入desc方法）
from sqlalchemy import desc
users = session.query(User).order_by(desc(User.name))

# 5.6 只查询部分属性
users = session.query(User.name).order_by(desc(User.name))
for user in users:
    print user.name

# 5.7 给结果集的列取别名
users = session.query(User.name.label('user_name')).all()
for user in users:
    print user.user_name

# 5.8 去重查询（需要导入distinct方法）
from sqlalchemy import distinct
users = session.query(distinct(User.name).label('name')).all()

# 5.9 统计查询
user_count = session.query(User.name).order_by(User.name).count()
age_avg = session.query(func.avg(User.age)).first()
age_sum = session.query(func.sum(User.age)).first()

# 5.10 分组查询
users = session.query(func.count(User.name).label('count'), User.age).group_by(User.age)
for user in users:
    print 'age:{0}, count:{1}'.format(user.age, user.count)

# 6.1 exists查询(不存在则为~exists())
from sqlalchemy.sql import exists
session.query(User.name).filter(~exists().where(User.role_id == Role.id))
# SELECT name AS users_name FROM users WHERE NOT EXISTS (SELECT * FROM roles WHERE users.role_id = roles.id)

# 6.2 除了exists，any也可以表示EXISTS
session.query(Role).filter(Role.users.any())

# 7 random
from sqlalchemy.sql.functions import random
user = session.query(User).order_by(random()).first()

session.close()


