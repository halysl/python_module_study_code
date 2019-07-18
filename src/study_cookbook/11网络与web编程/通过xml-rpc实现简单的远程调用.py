# -*- coding: utf-8 -*-
from xmlrpc.server import SimpleXMLRPCServer


class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
            # 关键的注册函数
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data.get(name, f"{name} not found")

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        try:
            return self._data.pop(name)
        except KeyError as e:
            return f"{name} not found"

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


# Example
if __name__ == '__main__':
    kvserv = KeyValueServer(('', 5201))
    kvserv.serve_forever()


"""
Client code
>>> from xmlrpc.client import ServerProxy
>>> s = ServerProxy('http://localhost:5201', allow_none=True)
>>> s.set('foo', 'bar')
>>> s.set('spam', [1, 2, 3])
>>> s.keys()
['spam', 'foo']
>>> s.get('foo')
'bar'
>>> s.get('spam')
[1, 2, 3]
>>> s.delete('spam')
>>> s.exists('spam')
False
>>>
"""
