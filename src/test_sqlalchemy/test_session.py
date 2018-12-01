# -*- coding:utf-8 -*-

from sqlalchemy import create_engine, func
from sqlalchemy import desc
from sqlalchemy import distinct
from sqlalchemy.sql import exists
from sqlalchemy.sql.functions import random
from sqlalchemy.orm import sessionmaker
from Models import Base, User, Role

DB_CONNECT_STRING = 'mysql+mysqlconnector://root:lightandwoqu@localhost:3306/test'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()

# 1. 创建表（如果表已经存在，则不会创建）
Base.metadata.create_all(engine)

# 2. 插入数据
u = User(name='tobi', age=200)
r = Role(name='user')

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
user0 = session.query(User).get(2)

# 5.2 返回结果集中的第2-3项
users0 = session.query(User)[1:3]

# 5.3 返回结果集中的所有项
users1 = session.query(User).all()

# 5.3 查询条件
user1 = session.query(User).filter(User.id < 6).first()

# 5.4 排序
users2 = session.query(User).order_by(User.name)

# 5.5 降序（需要导入desc方法）
users3 = session.query(User).order_by(desc(User.name))

# 5.6 只查询部分属性
users4 = session.query(User.name).order_by(desc(User.name))
for user in users4:
    print user.name

# 5.7 给结果集的列取别名
users5 = session.query(User.name.label('user_name')).all()
for user in users5:
    print user.user_name

# 5.8 去重查询（需要导入distinct方法
users6 = session.query(distinct(User.name).label('name')).all()

# 5.9 统计查询
user_count = session.query(User.name).order_by(User.name).count()
age_avg = session.query(func.avg(User.age)).first()
age_sum = session.query(func.sum(User.age)).first()

# 5.10 分组查询
users7 = session.query(func.count(User.name).label('count'), User.age).group_by(User.age)
for user in users7:
    print 'age:{0}, count:{1}'.format(user.age, user.count)

# 6.1 exists查询(不存在则为~exists())
session.query(User.name).filter(~exists().where(User.id == Role.id))
# SELECT name AS users_name FROM users WHERE NOT EXISTS (SELECT * FROM roles WHERE users.role_id = roles.id)

# 6.2 除了exists，any也可以表示EXISTS
session.query(Role).filter(Role.users.any())

# 7 random
user = session.query(User).order_by(random()).first()

session.close()

