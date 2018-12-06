# -*- coding: utf-8 -*-
# @Date    : 2018-12-06 16:52:17
# @Author  : Light (halysl0817@gmail.com)
# @Link    : ${link}
# @Version : 0.1
# @slogan: 狂风骤雨催纸伞，游人浪迹步不休，天地滂沱如何渡，蓑衣褪尽任浊流。
# @info: $info$

from collections import OrderedDict, MutableMapping, Mapping


class CaseInsensitiveDict(MutableMapping):
    """一个大小写不敏感的字典对象

    支持所有dict的方法。
    所有key都应该是字符串。
    重复的key（大小写不敏感）仅会记住最后一个。
    ``iter(instance)``,``keys()``, ``items()``, ``iterkeys()``和``iteritems()``会区分大小写。

    接着，比较也会是大小写不敏感，例如:
        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True
    """

    def __init__(self, data=None, **kwargs):
        self._store = OrderedDict()
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        # 存储key时默认为小写
        self._store[key.lower()] = (key, value)

    def __getitem__(self, key):
        # 根据传来的key的小写进行查询
        return self._store[key.lower()][1]

    def __delitem__(self, key):
        # 根据传来的key的小写进行删除
        del self._store[key.lower()]

    def __iter__(self):
        return (casedkey for casedkey, mappedvalue in self._store.values())

    def __len__(self):
        return len(self._store)

    def lower_items(self):
        """Like iteritems(), but with all lowercase keys."""
        return (
            (lowerkey, keyval[1])
            for (lowerkey, keyval)
            in self._store.items()
        )

    def __eq__(self, other):
        if isinstance(other, Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return NotImplemented
        # Compare insensitively
        return dict(self.lower_items()) == dict(other.lower_items())

    # Copy is required
    def copy(self):
        return CaseInsensitiveDict(self._store.values())

    def __repr__(self):
        return str(dict(self.items()))
