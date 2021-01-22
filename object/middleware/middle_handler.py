import os,re
from common import read_yaml
from common import path_config
from common import read_excel
from common import record_logger
from jsonpath import jsonpath
from common.conn_mysql import MysqlHandler
from common.handler_request import visit
from pymysql.cursors import DictCursor

class Handler:
    http=visit
    yaml_info=read_yaml.read_yaml(os.path.join(path_config.CONF_PATH,'conf.yml'))#配置文件内容
###excel
#这里的__表示此类的私有属性
    __casepath = os.path.join(path_config.CASE_PATH,'case.xlsx')# 获取excel文件的路径
    excel=read_excel.ExcelMethod(__casepath)# 初始化
#####日志
    def logger(self,name):
        __log_path = os.path.join(path_config.LOG_PATH,'logs')
        __log_info = self.yaml_info['log']
        Logger = record_logger.get_logger(name,__log_path,
                                           logger_level= __log_info['logger_level'],
                                           stream_level= __log_info['stream_level'],
                                           handler_level= __log_info['file_level'])
        return Logger

    @property#设置为属性，方便调用
    def token(self):
        return self.login()['token']


    def login(self):#用户登录
        userinfo=self.yaml_info['user_info']
        res = visit(url=userinfo['url'],
                    json=userinfo['json'])# 请求接口
        token = jsonpath(res,"$..token")[-1]
        return {'token': token}


    def replace_data(self,data):#正则匹配并替换
        while re.search(r'#(.+?)#',data):
            key=re.search(r'#(.+?)#',data).group(1)
            value=getattr(self,key,'')
            data=re.sub('#(.+?)#',str(value),data,1)
        return data


#数据库连接
class MidMysqlHandler(MysqlHandler):#继承封装好的MysqlHandler

    def __init__(self):
        mysqlinfo = Handler.yaml_info['mysqlinfo']#数据库的配置信息从config中获取
        super().__init__(host=mysqlinfo['host'],
                         user=mysqlinfo['user'],
                         password=mysqlinfo['password'],
                         database=mysqlinfo['database'],
                         port=mysqlinfo['port'],charset='utf8',cursorclass=DictCursor)

if __name__=="__main__":

   re=MidMysqlHandler().query("select nickname from users where mobile=17888888888")

   print(re['nickname'])