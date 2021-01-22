













import pytest

def test_one():
    assert 1==2

if __name__=="__main__":
    pytest.main(['-v','--reruns=2','--reruns-delay=3'])