def func(x):
    return x+1


def test_func():
    assert func(3) == 4


class TestClass(object):
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, '__str__')
