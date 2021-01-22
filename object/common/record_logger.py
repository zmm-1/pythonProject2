#日志方法
import logging
def get_logger(name=None,
               filepath=None,
               fmtt='%(name)s--%(asctime)s--%(lineno)d--%(levelname)s:%(message)s',
               logger_level='DEBUG',
               stream_level='DEBUG',
               handler_level='INFO'):
    logger = logging.getLogger(name)  # 初始化收集器
    # logger.handlers.clear()#清空收集器列表
    if not logger.handlers:
        logger.setLevel(logger_level)#设置日志等级
        stream_handler=logging.StreamHandler()#初始化处理器
        stream_handler.setLevel(stream_level)#设置处理器日志等级
        logger.addHandler(stream_handler)  # 处理器添加到收集器
        fmt = logging.Formatter(fmtt)  # 设置日志输出格式
        stream_handler.setFormatter(fmt)# 添加到处理器

        if filepath:
            file_handler=logging.FileHandler(filepath,'a',encoding='utf-8')#初始化文件输出处理器
            file_handler.setLevel(handler_level)#设置处理器日志等级
            file_handler.setFormatter(fmt)
            logger.addHandler(file_handler)  # 处理器添加到收集器
    return logger

if __name__=="__main__":
    get_logger()






