import  requests

#检查手机号是否已注册/post
#调用post方法，参数url，data，json...等
res=requests.post('http://tpad.api.zjxk12.com/zjx/api/user/checkRegister',json={"mobile":"18888888888"})
res=requests.request('post','http://tpad.api.zjxk12.com/zjx/api/user/checkRegister',json={"mobile":"18888888888"})

#get
res=requests.get('http://tpad.api.zjxk12.com/zjx/api/user/checkAccountAuth',
                 headers={'token':r'rNtq3i3wG4MKy1rZ1R1DMbqS5B4TmrgoUISK28EsZEQk5YSvqJdN1wbm4+MmRHx49QJkh1FGrM2FzQwchp0N/6j9sF1KK/GY'})
res=requests.request('get','http://tpad.api.zjxk12.com/zjx/api/user/checkAccountAuth',
                     headers={'token':r'rNtq3i3wG4MKy1rZ1R1DMbqS5B4TmrgoUISK28EsZEQk5YSvqJdN1wbm4+MmRHx49QJkh1FGrM2FzQwchp0N/6j9sF1KK/GY'})
print(res.json())#获取json格式的返回结果
print(res.status_code)#获取状态码
print(res.headers)#获取请求头信息
