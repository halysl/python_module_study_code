#MySql高级
##00.简介
* 实体与实体之间的3中对应关系，一对一，一对多，多对多
* 视图用于完成查询语句的封装
* 事务保证复杂的增删改查操作有效
* 为了提高查询速度，通过索引实现

##01.关系
* 建立成绩表score
        
        id
        学生
        科目
        成绩
* 学生列应该存放什么信息？
* 学生列的数据从学生表引用，关系也是一条数据；根据三大范式要求，这里引用学生表的id
* 同理，科目表也应该引自科目表（subject）中的数据
* 建立表的语句如下：

        create table scores(
        id int auto_increment primary key,
        score decimal(5,2),
        stuid int,
        subid int
        );
        
##02.外键
* 如何保证成绩表中stuid及subid有效？
* stuid可以通过外键约束进行有效性验证，即stuid的值必须在学生表的id列中出现过
* 完整的创建成绩表的指令如下：

        create table scores(
        id int auto_increment primary key,
        score decimal(5,2),
        stuid int,
        subid int，
        foreign key(stuid) references students(id),
        foreign key(subid) references subjects(id)
        );
        
##03.外键的级联操作
* 删除学生数据时，如果改id在其他表中（例如成绩表）已经存在，则会抛出异常
* 推荐使用逻辑删除
* 可以创建表时指定级联操作
* 语法如下：

        aalter table scores add constraint stu_sco foreign key(stuid) references students(id)
* 级联操作的类型包括：

        restrict（限制）：默认值，抛异常
        cascade（级联）：如果主表的记录删除，则从表中相关联的记录被删除
        set null：将外键设置为空
        no action：什么都不做
        
##04.连接查询
* 查询每个学生每个科目的分数
* 学生姓名来源于学生表，科目来源于科目表，成绩来源于成绩表，如何将三个表放在一起查询结果显示在一个结果集中，用连接查询
* 关键：找到对应的关系

        students表的id------scores表的stuid
        subjetcs表的id------scores表的subid
* 查询语句：

        select students.name,subjects.title,scores.score
        from scores
        inner join students on scores.stuid=students.id
        inner join subjects on scores.subid=subjects.id
        
* 连接查询的三种分类：

        表A inner join 表B：表A和表B匹配的行会出现在结果中
        表A left  join 表B：表A和表B匹配的行会出现在结果中，外加表A中独有的数据，未对应的数据使用null填充
        表A right join 表B：表A和表B匹配的行会出现在结果中，外加表B中独有的数据，未对应的数据使用null填充
        
* 练习
* 查询学生的姓名、平均分

        students.name
        avg(scores.score)
        关系:score.stuid=students.id
        分组:students.name
        
        select students.name,avg(scores.score)
        from scores
        inner join students on scores.suid=students.id
        group by students.name;

* 查询男生的姓名、总分

        students.name
        sum(scores.score)
        条件：sex=1 男生
        关系：scores.stuid = students.id
        分组：students.name
        
        select students.name,sum(scores.score)
        from scores
        inner join students on scores.stuid=students.id
        where students.sex=1
        group by students.name;

* 查询科目的名称、平均分

        subjects.title
        avg(scores.score)
        关系：scores.subid = subjects.id
        分组：subjects.title
        
        select subjects.title,avg(scores.score)
        from scores
        inner join subjects on scores.subid=subjects.id
        group by subjects.title;

* 查询未删除科目的名称、最高分、平均分

        subjects.title
        max(scores.score)
        avg(scores.score)
        条件：isdel=0 未删除
        关系：scores.subid = subjects.id
        分组：subjects.title
        
        select subjects.title,max(scores.score),avg(scores.score)
        from scores
        inner join subjects on scores.subid=subjects.id
        where subjects.isdel=0
        group by subjects.title;

##自关联
* 建立省表

        id
        title
* 建立市表

        id
        title
        proid（外键，连接省表的id）
* 两表的数据量统一，不会频繁的增加或减少，单独的生成两张不同的表会增加开销，故将两表合成一张表
* 观察两表结构发现市表比省表多一个字段，字段不可缺少，若并为一张表，则省份的proid为null
* 定义表areas，结构如下：

        id
        title
        pid
* 省对应的pid为null，城市对应的pid则填写省份的id
* 这就是自关联，表中的某一列，关联了这个表中的另一列，但是他们的业务逻辑是不同的
* 同理，该表可扩展区县划分（区县对应的pid为城市的id）
* 创建语句如下：

        create table areas(
        aid int primary key auto_increment not null,
        atitle varchar(20),
        pid int,
        foreign key(pid) references areas(id)
        );
* 从网上找到sql脚本，在mysql命令行中键入以下指令添加数据

        mysql -uroot -p
        password:******
        
        use dbname
        source areas.sql

* 查询一共多少数据

        select count(*)
        from areas;

* 查询一共多少省

        select count(*)
        from areas
        where pid is null;

* 查询安徽省有哪些城市：

        select title from areas where pid=(
        select id from areas where title='安徽省'
        );
        
        select city.* from areas as city
        inner join areas as province on city.pid=province.id
        where province.title='安徽省';

## 视图
* 对于复杂的查询，在多次使用过，维护是一件麻烦的时间
* 解决方案；定义视图
* 视图本质上就是对查询的一个封装
* 定义视图：

        create view view_name as
        select * from ...
* 查询视图：

        select * from view_name;
* 视图的本质是生成逻辑上的一张表

## 事务
* 当一个业务逻辑需要多个sql语句完成，将这些语句集合在一起，称为一个事务
* 使用事务可以完成退回的功能，保证业务逻辑的正确性
* 事务四大特性（ACID）：

        原子性：事务中的全部操作在数据库中是不可分割的，要么全部完成，要么全部不执行1
        一致性：几个并行执行的事务，其执行结果与无论以哪种方式串行执行事务，都一致
        隔离性：事务的执行不受到其他事物的干扰
        持久性：对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障

* 要求：表的类型必须是innodb或者bdb类型，才可使用事务
* 修改表的引擎

        alter table tbname engine=innodb;
* 事务语句：

        开始begin;
        提交commit;
        回滚rollback;

* 示例：

        步骤1：打开两个终端，连接mysql，使用同一个数据库，操作同一张表
        终端1：
        select * from students;
        ------------------------
        终端2：
        begin;
        insert into students(sname) values('张飞');
        
        
        
        步骤2
        终端1：
        select * from students;
        
        
        
        步骤3
        终端2：
        commit;
        ------------------------
        终端1：
        select * from students;

## 索引
* 在图书馆中，如何找到一本书？
* 当数据库中，数据量越大，查找数据越慢
* 索引能提高查找效率
* 主键和唯一索引，都是索引，可以提高查询速度
* 选择列的数据类型：

        越小的数据类型越好；
        简单的数据类型更好；
        尽量避免NULL；

* 索引分为单列索引和组合索引

        单列索引，即一个索引只包含单个列，一个表可以有多个单列索引
        组合索引，即一个索引包含多个列
* 查看索引

        show index from tbname;
* 创建索引：

        create index indexname on tbname(字段(length));
* 删除索引

        drop index indexname on tbname;
* 缺点：

        降低更新表的速度，更新表的同时索引文件也被更新
        索引文件占据磁盘空间