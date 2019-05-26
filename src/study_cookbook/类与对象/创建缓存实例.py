# -*- coding: utf-8 -*-
import weakref
_spam_cache = weakref.WeakValueDictionary()


class Spam:
    def __init__(self, name):
        self.name = name


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


def example_init_spam():
    a = get_spam('foo')
    b = get_spam('bar')
    print(a is b)
    c = get_spam('foo')
    print(a is c)


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
            self._cache.clear()


class Spam:
    manager = CachedSpamManager()

    def __init__(self, name):
        self.name = name

    def get_spam(name):
        return Spam.manager.get_spam(name)


if __name__ == "__main__":
    example_init_spam()
