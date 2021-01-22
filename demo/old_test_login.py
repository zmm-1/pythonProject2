
import pytest
import os#导入处理路径相关的模块
import json#从excel中拿出的数据需要转换成json格式
from common.read_excel import ExcelMethod#读取excel数据
from common.path_config import CASE_PATH,CONF_PATH,LOG_PATH#路径
from common.handler_request import visit#请求
from common.read_yaml import read_yaml#读取yaml的方法
from common.record_logger import get_logger#log方法
log_path=os.path.join(LOG_PATH,'log.txt')#生成log的文件
logger=get_logger('test_login',log_path)#初始化log方法
host=read_yaml(os.path.join(CONF_PATH,'conf.yml'))['pad_host']#从配置文件中拿到接口地址
path=os.path.join(CASE_PATH,'case.xlsx')#获取excel文件的路径
case=ExcelMethod(path).get_case('login')#根据sheet表单获取用例

@pytest.mark.parametrize('cases',case)#参数化
def test_login(cases):
    res=visit(url=host+cases['url'],json=json.loads(cases['data']))#请求接口，拿到实际结果

    try:
        assert res['code']==json.loads(cases['expected'])['code']#断言
        assert res['message'] == json.loads(cases['expected'])['message']
        logger.info('第{}条用例通过'.format(cases['case_id']))#日志记录
    except AssertionError as e:
        logger.error('第{}条用例失败,预期结果{}!=实际结果{}'.format(cases['case_id'], cases['expected'],res))#日志记录
        raise e
if __name__=="__main__":
    pytest.main(['-s','-v'])