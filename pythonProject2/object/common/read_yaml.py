#读取yaml文件方法
import yaml
def read_yaml(file):
    with open(file,encoding='utf-8') as f:
        config_info=yaml.load(f,Loader=yaml.SafeLoader)#通过yaml.load的方法
        return config_info











