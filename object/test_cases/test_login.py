import allure
import pytest
import json#从excel中拿出的数据需要转换成json格式
from middleware.middle_handler import Handler
logger=Handler().logger('login')#log
case=Handler.excel.get_case('login')#获取cases
host=Handler.yaml_info['pad_host']#获取接口地址

@allure.title("测试的登录功能")
@allure.feature('登录功能')
@allure.description("登录接口一共三个用例")
@allure.story("pad手机号密码登录的接口")
@pytest.mark.parametrize('cases',case)#参数化
def test_login(cases):

    res=Handler.http(url=host+cases['url'],json=json.loads(cases['data']))#请求接口，拿到实际结果

    try:
        assert res['code']==json.loads(cases['expected'])['code']#断言
        assert res['message'] == json.loads(cases['expected'])['message']
        logger.info('第{}条用例通过'.format(cases['case_id']))#日志记录
    except AssertionError as e:
        logger.error('第{}条用例失败,预期结果{}!=实际结果{}'.format(cases['case_id'], cases['expected'],res))#日志记录
        raise e
    except TypeError as e:
        logger.error('接口未请求成功')
        raise e

if __name__=="__main__":
    pytest.main(['-s'])