
import pytest


def test_one():
    assert 'i' not in 'is'
    print('断言成功')

def test_two():
    assert 2==2
    print('断言成功')


if __name__ == '__main__':
    pytest.main()