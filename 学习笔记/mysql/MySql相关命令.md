#MySql相关命令

##数据库连接
    mysql -u username -p
    password:*****
    
    mysql>

##数据库操作

创建数据库：

    create database dbname charsetutf-8;

删除数据库：

    drop database dbname;
    
切换数据库：

    use dbname;
    
查看当前选择的数据库：
 
    select database();
    
展示所有数据库：

    show databases;
    
##表操作
查看所有表：

    show tables;
    
创建表：

    create table tbname（
    列及类型约束
    ）;
    例如：
    create table students(
    id int auto_increment primary key,
    sname varcahr(10) not null
    );
    
修改表：

    alter table tbname add|change|drop 列名 类型;
    例如：
    alter table students add birthday datetime;
    
删除表：

    drop table tbname;
    
查看表结构：

    desc tbname;
    
更改表名称：

    rename table old-tbname to new-tbname;
    
查看表的创建语句：

    show create table tbname;
    
##数据操作：

查询：

    select * from tbname;
    
增加：

    全列插入：insert into tbname values(value);
    缺省插入：insert into tbname（列名） values（value）;
    同时插入多条：insert into tbname values(value1),(value2),(value3)...;
                insert into tbname(列名) values(value1),(value2),(value3)...;
                
 修改：
 
     update tbname set key1=value1,key2=value2 where 条件；
     
 删除：
 
     delete from tbname where 条件；
     
 逻辑删除：
     
     定义一个布尔字段，默认为1（存在），
     若需要删除，修改此值为0，
     查询中添加这个字段判断
     
##备份与恢复
数据备份：

    进入mysql库目录
    mysqldump -u username -p dbname > /backup.sql
    password:****
    
数据恢复：

    连接mysql，创建数据库
    推出连接
    mysql -u username -p dbname < /backup.sql
    password:****
    

    
