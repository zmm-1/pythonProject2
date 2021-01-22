
import os
dirname=(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#文件路径
CASE_PATH=(os.path.join(os.path.join(dirname,'data')))

#配置文件路径
CONF_PATH=(os.path.join(os.path.join(dirname,'config')))

#日志路径

LOG_PATH=(os.path.join(os.path.join(dirname,'logs')))

#测试报告路径

REPORT_PATH=(os.path.join(os.path.join(dirname,'report')))

#脚本路径

TEST_CASE=(os.path.join(os.path.join(dirname,'testcase')))




