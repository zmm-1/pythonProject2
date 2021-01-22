
import pytest

@pytest.fixture(scope='session')#定义fixtrue
def fix():
    print("执行前置条件")
