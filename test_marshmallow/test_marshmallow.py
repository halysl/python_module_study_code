# -*- coding:utf-8 -*-
"""
a docstring
"""
from datetime import date
from marshmallow import Schema, fields, pprint, post_load


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


class ArtistSchema(Schema):
    """艺术家的schema类"""
    name = fields.Str()


class AlbumSchema(Schema):
    """专辑的schema类"""
    title = fields.Str()
    release_date = fields.Date()
    artist = fields.Nested(ArtistSchema())

    @post_load()
    def make_album(self, data):
        """添加了post_load()装饰器的方法，在反序列化时会执行这个逻辑"""
        return Album(**data)


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
# 单个object的反序列化
# schema.load(dict) == dict-->dict
# schema.loads(str) == str-->dict
# if you want dict-->object, you should add a method in 'class AlbumSchema', then use the 'post_load()' decorator
origin_dict = schema.load(result_dict)
origin_str = schema.loads(result_str)
pprint(origin_dict)
pprint(type(origin_dict))
pprint(origin_str)
pprint(type(origin_str))


# 多个object，即objects-->list
alice = Artist(name='Alice')
bob = Artist(name='Bob')
cinderella = Artist(name='Cinderella')
alice_album = Album(title='To Alice', release_date=date(1971, 01, 01), artist=alice)
bob_album = Album(title='Kill Bob', release_date=date(1972, 02, 02), artist=bob)
cinderella_album = Album(title='Cinderella', release_date=date(1973, 03, 03), artist=cinderella)
album = [alice_album, bob_album, cinderella_album]

schema = AlbumSchema(many=True)
# 多个object的序列化
# schema.dump(obj_list) == obj_list-->dict_list
# schema.dumps(obj_list) == obj_list-->str
result_list = schema.dump(album)
result_str = schema.dumps(album)
pprint(result_list, indent=2)
pprint(result_str, indent=2)

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

print '==========================================================================================================='




print '==========================================================================================================='




