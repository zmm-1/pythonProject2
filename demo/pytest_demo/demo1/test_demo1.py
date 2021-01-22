


import pytest


class TestDemo:

    def test_one(self):
        assert 1 == 2

    def test_two(self):
        assert 2 == 3

    def test_three(self):
        assert 3 == 3


if __name__ == '__main__':
    pytest.main()