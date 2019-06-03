#!/usr/bin/env python
# -*- coding: utf-8 -*-

from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        # signature的用法是提取函数签名，可看方法 test_signature()
        sig = signature(func)
        # 然后对函数签名进行类型的绑定，.arguments是将 BoundArguments 对象转为一个 OrderedDict
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            # bound_values 就是将参数具体的包给函数签名
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, int)
def add(x, z):
    return x + z


def spam(x, y, z=10):
    pass


def test_signature():
    sig = signature(spam)
    print(sig)
    print(sig.parameters)
    bond_type = sig.bind_partial((int, float), int)
    print(bond_type)
    bond_type = bond_type.arguments
    print(bond_type)

if __name__ == "__main__":
    res = add(2, 3)
    print(res)
    test_signature()
