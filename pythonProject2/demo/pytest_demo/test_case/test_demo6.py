import pytest


@pytest.fixture(scope='module')#定义fixtrue
def fix():
    print("执行前置条件")

#测试用例
@pytest.mark.usefixtures('fix')
def test_one():#引用fixtrue
    assert 5==8


def test_two(fix):
    assert 9==9
if __name__=="__main__":
    pytest.main(['-s','-v'])

