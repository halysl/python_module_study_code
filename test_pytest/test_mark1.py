import pytest


@pytest.mark.a
def test_a_1():
    print('this is a')


@pytest.mark.a
def test_a_2():
    print('this is a')


@pytest.mark.b
def test_b_1():
    print('this is b')
