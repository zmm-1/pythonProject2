import pytest

# 登录功能
def login(username='', password=''):
    if username != '' and password != '':

        if username == 'admin' and password == '123456':  # 账号密码正确登录成功

            return {'msg': '登录成功'}

        else:  # 账号密码错误

            return {'msg': '账号或密码不正确'}

    return {'msg': '账号或密码为空'}  # 账号或密码为空

cases=[
{'case_id': 1,'title':'账号密码输入正确','data':{'username':'admin','password':'123456'},'expected':{'msg':'登录成功'}},
{'case_id': 2,'title':'账号或用户名不正确','data':{'username':'ADMIN','password':'123456'},'expected':{'msg':'账号或密码不正确'}},
{'case_id': 3,'title':'账号或密码为空','data':{'username':'','password':''},'expected':{'msg':'账号或密码为空'}}]


@pytest.mark.parametrize('case',cases)#参数化
def test_login(case):
    '''参数化结果：
    第一次：{'case_id':1,'title':'账号密码输入正确','data':{'username':'admin','password':'123456'},'expected':{'msg':'登录成功'}}
    第二次：{'case_id':2,'title':'账号或用户名不正确','data':{'username':'ADMIN','password':'123456'},'expected':{'msg':'账号或密码不正确'}}
    第三次：{'case_id':3,'title':'账号或密码为空','data':{'username':'','password':''},'expected':{'msg':'账号或密码为空'}}
    '''
    data=case['data']#获取请求参数data
    resaut=login(data['username'],data['password'])#调用被测函数，传入测试数据，获取实际结果
    assert case['expected']==resaut#预期结果与实际结果断言


if __name__=="__main__":
    pytest.main(['-s','-v'])