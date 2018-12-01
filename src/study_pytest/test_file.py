import pytest


@pytest.fixture(scope='module', autouse=True)
def openfile():
    print('open the file...')
    f = open('test.txt', 'a')
    return f

@pytest.mark.skip
def test_write1(openfile):
    old_tell = openfile.tell()
    data = '1111111111\n'
    openfile.write(data)
    new_tell = openfile.tell()
    assert new_tell - old_tell == len(data)


def test_write2(openfile):
    old_tell = openfile.tell()
    data = '2222222222\n'
    openfile.write(data)
    new_tell = openfile.tell()
    assert new_tell - old_tell == len(data)


def test_close(openfile):
    openfile.close()
    with pytest.raises(ValueError) as e:
        openfile.write('3')
