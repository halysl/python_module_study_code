# -*- coding:utf-8 -*-

from marshmallow import Schema, fields
from marshmallow import ValidationError, validate, validates


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
    # name必须存在
    name = fields.Str(required=True, data_key='id')
    # email必须正则匹配特定的规则
    email = fields.Email(
        validate=validate.Regexp('[0-9a-zA-Z.]+@woqutech.com'))
    # age可以通过设定validate进行值的范围判断
    # age = fields.Number(validate=lambda n: 18 <= n <= 41)
    # age = fields.Number(validate=validate.Range(18, 41))

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


user = {'name1': 123, 'age': 12, 'email': '123.45@woqutech.com'}

try:
    result = ValidUserSchema().load(user)
except ValidationError as e:
    print(e.message)


# 直接使用valid做数据校检，不生成object
errors = ValidUserSchema().validate(user)
print(errors)


u = {'id': 'a', 'age': 12, 'email': 'a@woqutech.com'}

load_result_dict = ValidUserSchema().load(u)

print(load_result_dict)
