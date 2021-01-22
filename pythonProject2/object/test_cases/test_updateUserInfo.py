import allure
import pytest
import json#从excel中拿出的数据需要转换成json格式
from middleware.middle_handler import Handler
logger=Handler().logger('modifyUserInfo')#log
case=Handler.excel.get_case('modifyUserInfo')#获取cases
host=Handler.yaml_info['pad_host']#获取接口地址
@allure.title("修改个人信息的接口")
@allure.feature('修改个人信息')
@pytest.mark.parametrize('cases',case)#参数化
def test_modifyUserInfo(cases,get_token,db_conn):#引用前置条件

    headers=cases['headers'].replace('#token#',get_token)#替换成前置条件中的token
    res=Handler.http(url=host+cases['url'],json=json.loads(cases['data']),headers=json.loads(headers))#请求接口，拿到实际结果
    try:
        if cases['case_id']==1:#判断为第一条修改nicakname的用例
            nickname=db_conn.query("select nickname from users where mobile='17888888888'")['nickname']#查询数据库的nickname
            assert nickname==json.loads(cases['data'])['nickname']#数据库中的nickname与请求时的nickname断言
        assert res['code']==json.loads(cases['expected'])['code']#断言
        assert res['message'] == json.loads(cases['expected'])['message']
        logger.info('第{}条用例通过'.format(cases['case_id']))#日志记录
    except AssertionError as e:
        logger.error('第{}条用例失败,预期结果{}!=实际结果{}'.format(cases['case_id'], cases['expected'],res))#日志记录
        raise e




