#MySql查询
##00.简介
* 查询基本语法：
            
        select * from tbname;
        
* from后面是表名
* select后面是列名，*代表着所有列
* 查询多列，以“，”分离
* distinct可以消除重复的行:
*     select distinct 列名字 from tbname; 

##01.条件
* 使用where子句对表中数据进行筛选，结果为true的行会出现在结果集中
* 语法类似于：

        select * from tbname where 条件;
        
###比较运算符
* 等于：=
* 大于：>
* 大于等于：>=
* 小于：<
* 小于等于：<=
* 不等于：!=或者<>

###逻辑运算符
* 与：and
* 或：or
* 非：not

###模糊查询
* 部分匹配方法
* 关键词：like
* %表示任意多个字符
* _表示任意一个字符

###范围查询
* in查询不连续的范围

        select * from tbname where id in（1，3，5);
        
* between...and...查询连续的范围

        select * from tbname where id between 1 and 5;
        
###空判断
* 判空关键字is null
* 例如：

        select * from tbname where id is null；
* 判断不为空关键字 is not null

### 优先级
* 小括号，not，比较运算符，逻辑运算符
* and优先级大于or




##02.聚合
* 为了快速得到统计数据而提供的五个聚合函数
* count(*)查询某结果集的总行数

        select count(*) from tbname;
        select count(*) from tbname where 条件;
* max（列名）求某列的最大值

        select max(列名) from tbname;
        select max(列名) from tbname where 条件;        
* min（列名）求某列的最小值

        select min(列名) from tbname;
        select min(列名) from tbname where 条件;
* sum（列名）求某列的和

        select sum(列名) from tbname;
        select sum(列名) from tbname where 条件;
* avg（列名）求某列的平均值

        select avg(列名) from tbname;
        select avg(列名) from tbname where 条件;

##03.分组
* 分组关键字：group by

        select 列1，列2，列3，聚合函数... from tbname group by 列1，列2.列3;
        
* 按照字段分组，表示此字段相同的数据会被放到一个组中
* 分组后，只能查询出相同的数据列，对于有差异的数据列无法出现在结果集中
* 可以对分组后的数据进行统计，做聚合运算
* 分组后的数据筛选：having

        select 列1，列2，聚合函数 from tbname 
        group by 列1，列2
        having 列1，列2，聚合;
        
##04.排序
* 为了方便查看数据，可以对数据进行排序
* 关键词：order by

        select * from tbname 
        order by 列1 asc|desc 列2 asc|desc;
* 默认为asc升序，可改为desc降序

##05.分页
* 数据过大时，可以分页查看
* 关键词：limit start count
* 从start开始，获取count条数据
* 例如：

        select * from tbname
        limit start，count;
        
##06.总结
* 完整的select语句

        select distinct *
        from 表名
        where ....
        group by ... having ...
        order by ...
        limit star,count
* 执行顺序：

        选择列，选择表，判断条件，分组，排序，分页。
