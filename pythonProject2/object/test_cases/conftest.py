import pytest
import jsonpath
from common.handler_request import visit
from middleware.middle_handler import Handler
from middleware.middle_handler import MidMysqlHandler
pad_host=Handler.yaml_info['pad_host']

# #获取token
@pytest.fixture(scope='module')
def get_token():
    res=visit(url=pad_host+'user/login',json={"mobile":"17888888888","password":"000000"},
              headers={"device":"ANDROID_868874030815988"})
    token=str(jsonpath.jsonpath(res,'$..token')[-1])
    token=token.replace('\n','')
    return token

#数据库连接
@pytest.fixture(scope='module')
def db_conn():
    db=MidMysqlHandler()#初始化
    db.query("UPDATE users set nickname='123' where mobile='17888888888'")#更新nickname，确保请求接口后发生变化
    db.conn.commit()#提交事务
    yield db
    db.mysql_close()#关闭数据库



