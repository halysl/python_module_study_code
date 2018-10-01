[TOC]
# marshmallow库的简单学习

marshmallow是一个简单序列化/反序列化模块。
它可以很轻松的做到
- `object-->dict`
- `objects-->list`

等序列化操作，同时经过添加简单的函数做到
- `dict-->object`
- `list-->objects`

等反序列化操作。
同时，它对于数据的校检非常友好，有多种校检方式，同时相对于Schema库，它可以更有针对性的校检数据，序列化数据等（例如只取某些数据，只校检某些数据等）。

## 一、简单说明

marshmallow库非常易于使用，下面将以实际的代码演示如何使用这个库。
先明确下使用流程。
创建类-->创建Schema类-->(创建ValidSchema类)
序列化<--->反序列化

## 二、创建Schema类

创建基础的类
```python
# -*- coding:utf-8 -*-

from datetime import date
from marshmallow import Schema, fields, pprint, post_load
from marshmallow import ValidationError, validate, validates

class Artist(object):
    """基础艺术家类"""
    def __init__(self, name):
        self.name = name


class Album(object):
    """基础专辑类"""
    def __init__(self, title, release_date, artist):
        self.title = title
        self.release_date = release_date
        self.artist = artist
```
根据自己的类创建对应的Schema类，继承自marshmallow的Schema类。
```python
class ArtistSchema(Schema):
    """艺术家的schema类"""
    name = fields.Str()


class AlbumSchema(Schema):
    """专辑的schema类"""
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())
```
可以观察到，Schema类的字段和基础类的成员命名一致，在这里先保持一致，后面会对字段进一步说明；同时可以观察到Schema里对数据类型进行了限定，例如title只能是字符串，release_date只能是日期格式，这算是数据校检的第一步类型校检。

## 三、序列化和反序列化

### 1、定义

我之前一直不能理解什么是序列化，什么是反序列化，它到底有什么用。
维基定义是【序列化（serialization）在计算机科学的资料处理中，是指将数据结构或物件状态转换成可取用格式（例如存成档案，存于缓冲，或经由网络中传送），以留待后续在相同或另一台计算机环境中，能恢复原先状态的过程。依照序列化格式重新获取字节的结果时，可以利用它来产生与原始物件相同语义的副本。】
通俗的说法就是将一个数据处理成可以存储或者传输的形式，这个过程叫序列化，反过来，将某种形式的数据处理成可以使用的数据就是反序列化。
举个python上的例子。python有个内建dict类型，也就是字典类型，可以方便的处理键值对数据，这个数据暂存于内存中，如何将它保存或者将它传输，最简单的方法就是json.dump()，将数据保存在json文件里，这个过程就称之为序列化。反过来，你拿到了一个json文件，通过json.load()，将json文件里的数据转成了dict就可以直接使用，这个过程就称之为反序列化。

### 2、序列化

marshmallow可以对一个object进行序列化成一个dict，同时可以对一群object进行序列化成一个list。
单个object的序列化：
下面是序列化的操作，可以看到进行了两次序列化，一次输出成dict类型，一次输出成str类型。
```python
# 单个object，即object-->dict
bowie = Artist(name='David Bowie')
album = Album(artist=bowie, title='Hunky Dory', release_date=date(1971, 12, 17))

schema = AlbumSchema()
# 单个object的序列化
# schema.dump(obj) == obj-->dict
# schema.dumps(obj) == obj-->str
result_dict = schema.dump(album)
result_str = schema.dumps(album)

pprint(result_dict, indent=2)
pprint(type(result_dict))
pprint(result_str, indent=2)
pprint(type(result_str))
```
这是输出的结果。
```txt
{ u'artist': { u'name': u'David Bowie'},
  u'release_date': '1971-12-17',
  u'title': u'Hunky Dory'}
<type 'dict'>
'{"release_date": "1971-12-17", "title": "Hunky Dory", "artist": {"name": "David Bowie"}}'
<type 'str'>
```
序列化之后我们就可以进行保存或者传输，dict存储为json，str存储为文本。

多个object的序列化：
下面是序列化的操作，可以看到进行了两次序列化，一次输出成list类型，其中list的每一个元素都是dict类型，一次输出成str类型。`多个object序列化不需要变动Schema类，只要添加many=True这个属性就可以了。`
```python
# 多个object，即objects-->list
alice = Artist(name='Alice')
bob = Artist(name='Bob')
cinderella = Artist(name='Cinderella')
alice_album = Album(title='To Alice', release_date=date(1971, 01, 01), artist=alice)
bob_album = Album(title='Kill Bob', release_date=date(1972, 02, 02), artist=bob)
cinderella_album = Album(title='Cinderella', release_date=date(1973, 03, 03), artist=cinderella)
album = [alice_album, bob_album, cinderella_album]

## Schema类字段many=True
schema = AlbumSchema(many=True)
# 多个object的序列化
# schema.dump(obj_list) == obj_list-->dict_list
# schema.dumps(obj_list) == obj_list-->str
result_list = schema.dump(album)
result_str = schema.dumps(album)
pprint(result_list, indent=2)
pprint(result_str, indent=2)
```
这是输出的结果。
```txt
[ { u'artist': { u'name': u'Alice'},
    u'release_date': '1971-01-01',
    u'title': u'To Alice'},
  { u'artist': { u'name': u'Bob'},
    u'release_date': '1972-02-02',
    u'title': u'Kill Bob'},
  { u'artist': { u'name': u'Cinderella'},
    u'release_date': '1973-03-03',
    u'title': u'Cinderella'}]
'[{"release_date": "1971-01-01", "title": "To Alice", "artist": {"name": "Alice"}}, {"release_date": "1972-02-02", "title": "Kill Bob", "artist": {"name": "Bob"}}, {"release_date": "1973-03-03", "title": "Cinderella", "artist": {"name": "Cinderella"}}]'
```
序列化之后我们就可以进行保存或者传输，list不能直接存储，但是可以作为dict的一个value存储为json，str存储为文本。

### 3、反序列化

marshmallow可以对一个dict或str进行反序列化成一个`object`，同时可以对一个list或str进行反序列化成一个list，此时list的每个元素是`object`。
注意：marshmallow默认并不能反序列化成`object`，但添加一个简单的方法就可以实现。

```python
class AlbumSchema(Schema):
    """专辑的schema类"""
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

    @post_load()
    def make_album(self, data):
        """添加了post_load()装饰器的方法，在反序列化时会执行这个逻辑"""
        return Album(**data)
```

单个object的反序列化：
下面是反序列化的操作，可以看到进行了两次反序列化，一次将dict类型输出成`object`，一次将str类型输出`object`。
```python
# 单个object的反序列化
# schema.load(dict) == dict-->dict
# schema.loads(str) == str-->dict
# if you want dict-->object, you should add a method in 'class AlbumSchema', then use the 'post_load()' decorator
# result_dict  result_str是序列化后的结果
origin_dict = schema.load(result_dict)
origin_str = schema.loads(result_str)
pprint(origin_dict)
pprint(type(origin_dict))
pprint(origin_str)
pprint(type(origin_str))
```
这是输出的结果。
```txt
<__main__.Album object at 0x7f4784e48c10>
<class '__main__.Album'>
<__main__.Album object at 0x7f4784e48b90>
<class '__main__.Album'>
```
可以看出已经变成了对象。

多个object的反序列化：
```python
# 多个object的反序列化
# schema.load(list) == list-->list
# schema.loads(str) == str-->list
# 在这里，反序列化后会生成三个对象的列表，即列表的每一个元素都是一个实例
origin_list = schema.load(result_list)
origin_str = schema.loads(result_str)
pprint(origin_list)
pprint(type(origin_list))
pprint(origin_str)
pprint(type(origin_str))
```
以下是结果，可以很清楚的看到反序列化为了一个list，list的每个元素是`object`。
```txt
[<__main__.Album object at 0x7f51eb7ebed0>,
 <__main__.Album object at 0x7f51eb7ebf10>,
 <__main__.Album object at 0x7f51eb7ebf50>]
<type 'list'>
[<__main__.Album object at 0x7f51eb7ebf90>,
 <__main__.Album object at 0x7f51eb7ebfd0>,
 <__main__.Album object at 0x7f51eb781050>]
<type 'list'>
```
### 4、部分序列化
之前的序列化都是对object完整的序列化操作，假设现在只需要传输或者保存object的某些字段该怎么做？Schema类提供了一个only属性，只序列化only内的字段。
```python
# 不加only
schema = AlbumSchema()
result = schema.dump(alice_album)
pprint(result)
# 添加only=['title', 'release_date']
schema = AlbumSchema(only=['title', 'release_date'])
result = schema.dump(alice_album)
pprint(result)
```
```txt
# 不加only输出结果
{u'release_date': '1971-01-01', u'title': u'To Alice', u'artist': {u'name': u'Alice'}}
# 添加only输出结果
{u'release_date': '1971-01-01', u'title': u'To Alice'}
```
我们需要哪些字段就将哪些字段加到only列表中，这样可以减少序列化后的数据量，传输也更轻松。

### 5、部分反序列化(这部分应放在特殊用法)

[官方文档(https://marshmallow.readthedocs.io/en/3.0/quickstart.html)  这部分的标题是Partial Loading，意为部分加载，它指的是可以不对Schema类里的所有字段进行校检。

举个简单的例子，定义了一个有十个字段的类，又定义了一个相关的Schema类。假设我需要对传来的部分数据做校检该怎么做？直接放进schema.load()必定会出错，这时候就需要用到partial属性。
（但还是会有个前提，即Schema类中不实现生成对象的方法）。

## 四、数据校检

终于来到了数据校检部分。数据校检可以简单地分为数据类型检查和数据值的检查。marshmallow的数据校检过程中甚至可以主动格式化传来的数据，例如使其大写或者小写等。

- fields类型校检
- fields的required属性校检
- fields的validate属性校检
- fields的method校检

可以看出，主要是围绕fields进行校检，在看校检过程之前先解释下ValidationError和Field概念。

`ValidationError：marshmallow里的错误类型，通过try——except捕捉到这个错误后，可以直接输出message信息，它将以字典形式放回所有校检失败的原因`
`Field：各种类型数据的字段类`

下面将直接通过代码说明校检过程。

```python
class User(object):
    """用户类"""
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


class UserSchema(Schema):
    """user普通schema类"""
    name = fields.Str()
    age = fields.Number()
    email = fields.Email()


class ValidUserSchema(UserSchema):
    """
    user有效值判断schema
    有多种判断方式
    """
    # 先是判断name是不是Str类型
    # fields添加了required=True属性，指的是name必须存在
    name = fields.Str(required=True)
    
    # 先是判断email是不是Email类型
    # field添加了validate属性，validate可以用多种方式校检，这里用到的是正则匹配
    # email必须正则匹配特定的规则
    email = fields.Email(validate=validate.Regexp('[0-9a-zA-Z.]+@woqutech.com'))
    # age可以通过设定validate进行值的范围判断
    age = fields.Number(validate=lambda n: 18 <= n <= 41)
    age = fields.Number(validate=validate.Range(18, 41))
    
    # 下面是fields的method校检方式
    age = fields.Number()

    @validates('age')
    def validate_age(self, value):
        """
        age同样可以通过method进行值的判断，需要装饰器validates(key_name)
        """
        if value < 0:
            raise ValidationError('Age should not < 0')
        if value > 100:
            raise ValidationError('Age should not > 100')


user = {'name': 'Alice', 'age': -12, 'email': '123.4?5@woqutech.com'}

try:
    result = ValidUserSchema().load(user)
except ValidationError as e:
    print(e.message)
```

## 五、特殊用法

- Partial Loading
- Handling Unknown Fields
- Schema.validate
- Specifying Attribute Names
- Specifying Serialization/Deserialization Keys
- Refactoring: Implicit Field Creation
- Ordering Output
- “Read-only” and “Write-only” Fields
- Specify Default Serialization/Deserialization Values


参考文档：
[快速开始](https://marshmallow.readthedocs.io/en/3.0/quickstart.html)
[marshmallow官方文档](https://marshmallow.readthedocs.io/en/3.0/)

