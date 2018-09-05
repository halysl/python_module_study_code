# -*- coding:utf-8 -*-
import yaml
from schema import Schema, Use


def aaa(schema):
    try:
        with open('../conf/dbinfo.yaml', 'r') as f:
            data = yaml.load(f)
            schema.validate(data)
            for key in data.keys():
                for item in data[key]:
                    print(item)
            print(data)
    except yaml.parser.ParserError as e:
        print('请检查你的yaml文件')
        print(e)
    except IOError as e:
        print('文件不存在')
        print(e)
    except yaml.scanner.ScannerError as e:
        print('yaml解析错误，请检查')


schema1 = Schema(
    {
        Use(str):
            [
                {'ip': Use(str), 'sidn': Use(str), 'sid': Use(str), 'port': Use(int)}
            ]
    }
)

aaa(schema1)