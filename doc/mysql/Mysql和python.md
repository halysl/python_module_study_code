#MySql和Python
##安装引入模块
* 使用接口Python DB API
* 安装mysql模块

        pip install mysql-connector-python #python2.7，使用Python-MySQL connector
        pip install pymysql #python3.4，安装pymysql模块            
        
* 引入模块

        import pymsql #python3.x
        import mysql.connector #py2.x
        
##connection对象
* 用于建立与数据库的连接
* 创建方法：

        conn = pymysql.Connect(host,port,user,passwd,db) #py3.x
        
        host：连接的mysql主机，本机填为‘localhost’
        port：连接的mysql主机的端口，默认为3306
        user：连接的用户名
        passwd：连接的用户的密码
        db：连接的数据库名

* connection对象的方法

        close()：关闭连接
        commit()：提交修改
        rollback()：回滚事务
        cursor()：返回cursor对象

## cursor对象
* 用于执行语句
* 创建方法：

        cursor = conn.cursor()

* 方法

        execute(op,[args])，执行一个数据库查询和命令
		 fetchone()，取得结果集的下一行
		 fetchmany(size)，取得结果集的下几行
		 fetchall()，取得结果集的剩下的所有行
		 rowcount，最近一次execute返回数据的行数或影响行数
		 close()，关闭游标对象
* 属性

        rowcount只读属性，表示最近一次execute()执行后受影响的行数
        connection获得当前连接对象

## 查询的一般流程
* select查询数据操作过程：

        开始
        创建connection
        创建cursor
        使用cursor.excute()执行select语句
        使用cursor.fetch*()获取并处理数据
        关闭cursor
        关闭connection
        结束

## 常见查询语句

        #增加
        import pymysql
        try:
            conn = pymysql.Connect(host,port,user,passwd,db)
            cs1=conn.cursor()
            count=cs1.execute("insert into students(sname) values('张良')")
            print(count)
            conn.commit()
            cs1.close()
            conn.close()
        except Exception,e:
            print e.message
            
        
        #删除
        #encoding=utf-8
        import pymysql
        try:
            conn = pymysql.Connect(host,port,user,passwd,db)
            cs1=conn.cursor()
            count=cs1.execute("delete from students where id=6")
            print(count)
            conn.commit()
            cs1.close()
            conn.close()
        except Exception,e:
            print e.message
            
            
        #查询一行数据
        #encoding=utf8
        import pymysql
        try:
            conn = pymysql.Connect(host,port,user,passwd,db)
            cur=conn.cursor()
            cur.execute('select * from students where id=7')
            result=cur.fetchone()
            print()
            cur.close()
            conn.close()
        except Exception,e:
            print e.message
            
            
        #查询多行数据
        #encoding=utf8
        import pymysql
        try:
            conn = pymysql.Connect(host,port,user,passwd,db)
            cur=conn.cursor()
            cur.execute('select * from students')
            result=cur.fetchall()
            print(result)
            cur.close()
            conn.close()
        except Exception,e:
            print e.message
            
## sql语句参数化
* 以参数传递的方式执行sql脚本，为之后的封装打基础
* 例如：

        #encoding=utf-8
        import pymysql
        try:
            conn = pymysql.Connect(host,port,user,passwd,db)
            cs1=conn.cursor()
            sname=raw_input("请输入学生姓名：") #参数
            params=[sname] #参数封装成列表
            count=cs1.execute('insert into students(sname) values(%s)',params) #%传参
            print(count)
            conn.commit()
            cs1.close()
            conn.close()
        except Exception,e:
            print e.message

## 封装
* 将常见的语句封装成方法，以传参的方式执行语句
* 例如：

        #encoding=utf8
        import pymysql
        class MysqlHelper():
            def __init__(self,host,port,db,user,passwd,charset='utf8'):
                self.host=host
                self.port=port
                self.db=db
                self.user=user
                self.passwd=passwd
                self.charset=charset
            
            def connect(self):
                self.conn=MySQLdb.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
                self.cursor=self.conn.cursor()
            
            def close(self):
                self.cursor.close()
                self.conn.close()
            
            def get_one(self,sql,params=()):
                result=None
                try:
                    self.connect()
                    self.cursor.execute(sql, params)
                    result = self.cursor.fetchone()
                    self.close()                    
                except Exception, e:
                    print e.message
                return result
            
            def get_all(self,sql,params=()):
                list=()
                try:
                    self.connect()
                    self.cursor.execute(sql,params)
                    list=self.cursor.fetchall()
                    self.close()
                except Exception,e:
                    print e.message
                return list
            
            def insert(self,sql,params=()):
                return self.__edit(sql,params)
                
            def update(self, sql, params=()):
                return self.__edit(sql, params)
            
            def delete(self, sql, params=()):
                return self.__edit(sql, params)
            
            def __edit(self,sql,params):
                count=0
                try:
                    self.connect()
                    count=self.cursor.execute(sql,params)
                    self.conn.commit()
                    self.close()
                except Exception,e:
                    print e.message
                return count