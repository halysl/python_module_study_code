[TOC]

# Schema库的简单学习

Schema是一个简单易用的python数据校检三方库，[Schema on Github](https://github.com/keleshev/schema).

在web app中，经常需要接收用户传过来的数据，然后做处理。但是用户由于各种原因，输入的数据并不如人意。前端发送json形式数据到后端api，以往的解决方案甚是暴力，对json的key的值进行各种if检验，甚至要去做正则匹配。使用schema库能够非常优雅的解决这个问题。

Schema和marshmallow的取舍。之前学习过marshmallow，它有一个方法Schema.validate，同样可以完成数据校检，但是需要先生成一个独特的Schema类，用起来更适合序列化/反序列化的场景。而Schema库只做一件事，那就是数据校检。

## 核心类
- Schema  数据检验最重要的类
- Regex  正则匹配检验用到的类
- Use
- And
- Or

## 一个类、一个方法
这是schema库里最重要的概念。
- 一个类是Schema类，可以理解为schema库的入口，什么都可以往里面传。
- 一个方法是validate方法，它接入一个数据或者一个obj。
- 执行校检就是处理validate接收的数据和Schema类接收的schema之间的关系。

## Schema类传入基础类型`str,int,float,object`
```python
>>> from schema import Schema
>>> Schema(str).validate('abc')
'abc'
>>> Schema(int).validate(123)
123
>>> Schema(float).validate(1.23)
1.23
>>> Schema(object).validate('abcd')
'abcd'
>>> Schema(str).validate(123)
schema.SchemaUnexpectedTypeError: 123 should be instance of 'str'
```

基础类型没什么好说的，只能检验最简单的数据。注意object是基类，也就是validate里的数据符合语法就会原样输出，但我们可以基于此做些类的判断

```python
>>> from schema import Schema
>>> from datetime import datetime as dt
>>> now = dt(2018, 8, 30)
>>> Schema(object).validate(now)
datetime.datetime(2018, 8, 30, 0, 0)
>>> Schema(dt).validate(now)
datetime.datetime(2018, 8, 30, 0, 0)
```

到这里，可以发现有点像[isinstance](http://www.runoob.com/python/python-func-isinstance.html)，看了下代码，果然是这么实现的...

## Schema类传入可调用的对象`func，class with __call__`
```python
>>> from schema import Schema
>>> import os
>>> Schema(os.path.exists).validate('/home/light')
'/home/light'
>>> Schema(os.path.exists).validate('/thgil/emoh')
schema.SchemaError: exists('/thgil/emoh') should evaluate to True
>>> Schema(lambda n: n > 0).validate(123)
123
>>> Schema(lambda n: n > 0).validate(-12)
SchemaError: <lambda>(-12) should evaluate to True
```
可以看到，当Schema类传入的是可调用对象，那么它会将validate里的数据传入可调用对象，当可调用对象返回的值不为False就返回值。

```python
# 底层实现
# schema指的是有__call__方法的对象
if schema(data):
    return data
```

## Schema类传入带有validate方法的对象`And，Or，Use，Regex，Const`

If Schema(...) encounters an object with method validate it will run this method on corresponding data as data = obj.validate(data). This method may raise SchemaError exception, which will tell Schema that that piece of data is invalid, otherwise—it will continue validating.
渣翻：如果Schema类传入了带有validate方法的对象，那么将不使用Schema自己的validate方法，而是转给那个对象去执行。
举个栗子：
```python
>>> from schema import Schema,And,Or,Use,Regex,Const
>>> Schema(And(int, lambda x:x>10)).validate(20)
20
>>> And(int, lambda x:x>10).validate(20)
20
```

### Regex正则匹配
```python
>>> Regex(r'^foo').validate('foobar')
'foobar'
>>> Schema(Regex(r'^foo')).validate('foobar')
'foobar'
>>> Regex(r'^[A-Z]+$', flags=re.I).validate('those-dashes-dont-match')
schema.SchemaError: Regex('^[A-Z]+$', flags=re.IGNORECASE) does not match 'those-dashes-dont-match'
>>> Regex(r'^[A-Z-]+$', flags=re.I).validate('those-dashes-will-match')
'those-dashes-will-match'
```
正则表达式需要用到re库。flags是re里的概念，re.I可以理解为忽略大小写。

### And且
看到and，or肯定能想到与或非门。and就有点与的想法。
```python
>>> And(int, lambda x:x>10).validate(20)
20
>>> And(str, Regex(r'^[a-zA-Z0-9]+')).validate('asdwasd')
'asdwasd'
>>> And(str, Regex(r'^[a-zA-Z0-9]'), lambda x:len(x)<10).validate('qwertyu')
'qwertyu'
>>> And(str, Regex(r'^[a-zA-Z0-9]'), lambda x:len(x)<10).validate('qwertyuiopasdfghjkl')
schema.SchemaError: <lambda>('qwertyuiopasdfghjkl') should evaluate to True
```
第一个例子，需要数据是int类型并且大于10；第二个例子，需要数据是字符串，并且正则匹配下成功；第三个例子，需要数据是字符串，并且正则匹配下成功，并且长度小于10.

### Or或
```python
>>> Or(str, int, float).validate('abc')
'abc'
>>> Or(str, int, float).validate(123)
123
>>> Or(str, int, float).validate(1.23)
1.23
>>> Or(Regex(r'^[a-zA-Z0-9]'), lambda x:len(x)<10).validate('qwertyuiopasdfghjkl')
'qwertyuiopasdfghjkl'
```
### Use创建数据
Use的用法有点不像是校检，而是格式化数据。
```python
>>> Use(str).validate(123)
'123'
>>> Use(int).validate('123')
123
>>> Use(int).validate('abc')
schema.SchemaError: int('abc') raised ValueError("invalid literal for int() with base 10: 'abc'",)
```
它会尝试着将validate的数据转换为指定的类型。单独的使用可能作用不大，但在后面的字典校验中作用很大。

### Const常量
const的使用同样不像是校检，而是为了数据安全。
Sometimes you need to transform and validate part of data, but keep original data unchanged. Const helps to keep your data safe。
看了下底层代码，并不能理解为什么这样就能保证数据的安全。
```python
>>> from schema import Use, Const, And, Schema
>>> from datetime import datetime
>>> is_future = lambda date: datetime.now() > date
>>> to_json = lambda v: {"timestamp": v}
>>> Schema(And(Const(And(Use(datetime.fromtimestamp), is_future)), Use(to_json))).validate(1234567890)
{"timestamp": 1234567890}
>>> Schema(And(And(Use(datetime.fromtimestamp), is_future), Use(to_json))).validate(1234567890)
{'timestamp': datetime.datetime(2009, 2, 14, 7, 31, 30)}
```
可以看到添加了const的数据直接保留传入数据，而不是通过datetime.fromtimestamp()方法转成实际年月日。

##  Schema类传入容器对象`list，tuple，set，frozenset`
```python
>>> Schema([1, 0]).validate([1, 1, 0, 1])
[1, 1, 0, 1]
>>> Schema((int, float)).validate((5, 7, 8, 'not int or float here'))
SchemaError: Or(<type 'int'>, <type 'float'>) did not validate 'not int or float here'
'not int or float here' should be instance of 'float'
```
简单理解就是，validate的值可以匹配到Schema里的任何一项就ok。
对于validate数据就是遍历。
对于Schema的schema就是or。

## Schema类传入字典
这一段是最重要的，毕竟现在前后端传递数据还是使用的json格式，也就是键值对，也可以转成字典数据。

定义两个概念：
- `模式字典`：Schema类里使用的字典，会有各种形式
- `数据字典`：validate方法里的字典，可以当做普通的字典

```python
# 常见用法，key固定检验value值；或者key和value都要检查
>>> Schema({'name': str, 'age': lambda n: 18 <= n <= 99}).validate({'name': 'Sue', 'age': 28})
{'age': 28, 'name': 'Sue'}
>>> Schema({str: int, int: None}).validate({'key1': 1, 2: None})
{2: None, 'key1': 1}
>>> Schema({str: int, int: None}).validate({'key1': 1, 2: 2})
SchemaError: Key '2' error: None does not match 2
```
```python
# 特殊用法
# 看第二个validate测试会很奇怪，为什么模式字典三项，而数据字典可以有四项。
# 理解就是数据字典的每一项只要可以匹配模式字典，并且模式字典都被匹配过，就算成功匹配。
>>> schema = Schema({'key1': str,'key2': str, str: object})
>>> schema.validate({'key1': 'a','key2': 'b','key3': 'c'})
{'key1': 'a', 'key2': 'b', 'key3': 'c'}
>>> schema.validate({'key1': 'a','key2': 'b','key3': 'c', 'key4': 1})
{'key1': 'a', 'key2': 'b', 'key3': 'c', 'key4': 1}
>>> schema.validate({'key1': 'a','key2': 'b'})
SchemaMissingKeyError: Missing keys: <type 'str'>
# 上面可能有点绕，我们引入一个新的类optional，它的意思就是可选，也就是这个key在不在都行。
>>> schema = Schema({'name': str, Optional('occupation'): str})
>>> schema.validate({'name': 'Sam', 'occupation': '1'})
{'name': 'Sam', 'occupation': '1'}
>>> schema.validate({'name': 'Sam'})
{'name': 'Sam'}
# 结合上面两个注释的解释，我们可以写出一个特殊的匹配。
# 下面的匹配模式意思是，接受一个学生字典，必须要有id（数字且大于0），名字（字符串），年龄（数字且大于8），其他项目。
>>> student_schema = Schema({'id': And(int, lambda x: x>0), 'name': str, 'age':And(int, lambda x: x>8), Optional(str):object})
>>> student_schema.validate({'id': 1, 'name': 'Ash', 'age': 12})
{'age': 12, 'id': 1, 'name': 'Ash'}
>>> student_schema.validate({'id': 1, 'name': 'Ash', 'age': 12, 'sex': 'girl'})
{'age': 12, 'id': 1, 'name': 'Ash', 'sex': 'girl'}
>>> student_schema.validate({'id': 2, 'name': 'Bob', 'age':14, 'city': 'hz', 'sex': 'boy'})
{'age': 14, 'city': 'hz', 'id': 2, 'name': 'Bob', 'sex': 'boy'}
# 我们对学生匹配模式做个假定，倘若性别不写就是’null‘，城市不写就是’hz‘.
# Optional的default字段
>>> student_schema = Schema({'id': And(int, lambda x: x>0), 'name': str, 'age':And(int, lambda x: x>8), Optional('sex', default='null'): str, Optional('city', default='hz'): str, Optional(str): object})
>>> student_schema.validate({'id': 1, 'name': 'Ash', 'age': 12})
{'age': 12, 'city': 'hz', 'id': 1, 'name': 'Ash', 'sex': 'null'}
>>> student_schema.validate({'id': 1, 'name': 'Ash', 'age': 12, 'sex': 'girl'})
{'age': 12, 'city': 'hz', 'id': 1, 'name': 'Ash', 'sex': 'girl'}
>>> student_schema.validate({'id': 2, 'name': 'Bob', 'age':14, 'city': 'zh', 'sex': 'boy'})
{'age': 14, 'city': 'zh', 'id': 2, 'name': 'Bob', 'sex': 'boy'}
# 最后一个类Forbidden，禁止数据字典出现某个key
>>> from schema import Forbidden
>>> Schema({Forbidden('age'): object}).validate({'age': 50})
SchemaForbiddenKeyError: Forbidden key encountered: 'age' in {'age': 50}
>>> Schema({Forbidden('age'): str, 'age': int}).validate({'age': 50})
{'age': 50}
```
## Schema的ignore_extra_keys字段
```python
>>> schema = Schema({'name': str}, ignore_extra_keys=True)
>>> schema.validate({'name': 'Sam', 'age': '42'})
{'name': 'Sam'}
```

## 友好的错误提示
schema库默认的错误提示抛去堆栈的报错，最后一行的报错信息已经足够，但是schema提供了一个自定义报错提示的接口。
You can pass a keyword argument error to any of validatable classes (such as Schema, And, Or, Regex, Use) to report this error instead of a built-in one.
```python
>>> Schema(Use(int, error='Invalid year')).validate('XVII')
Traceback (most recent call last):
...
SchemaError: Invalid year
```
