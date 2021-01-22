#
# import pytest
#
#
# b=[(1,2,3),['a','b','c'],{'id':2}]#测试数据
#
# @pytest.mark.parametrize('list',b)#接受两个参数
# def test_login(list):#作为用例参数，接受装饰器传入的参数
#     print('\na的值为:{}'.format(list))
#
#
# if __name__=="__main__":
#     pytest.main(['-s','-v'])