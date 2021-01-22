import  requests


#检查手机号是否已注册/post
#调用post方法，参数url，data，json...等
res1=requests.post('http://tpad.api.zjxk12.com/zjx/api/user/checkRegister',json={"mobile":"18888888888"},data=None)

print(res1.json())#获取json格式的返回结果
print(res1.status_code)#获取状态码
print(res1.headers)#获取请求头信息
