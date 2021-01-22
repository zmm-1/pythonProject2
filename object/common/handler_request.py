#重新封装request
import requests

def visit(url,method='post',params=None,data=None,json=None,files=None,**kwargs):
    res=requests.request(method,url,params=params,data=data,json=json,files=files,**kwargs)
    try:
        return res.json()#返回json格式
    except Exception as e:
        print("格式错误{}".format(e))







