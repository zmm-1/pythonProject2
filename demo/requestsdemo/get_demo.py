import  requests
#检查账号是否有权限/get
#调用get方法，参数url，params，headers....等
res=requests.get('http://tpad.api.zjxk12.com/zjx/api/user/checkAccountAuth',
                 params=None,headers={'token':r'rNtq3i3wG4MKy1rZ1R1DMbqS5B4TmrgoUISK28EsZEQk5YSvqJdN1wbm4+MmRHx49QJkh1FGrM2FzQwchp0N/6j9sF1KK/GY'})
print(res.json())#json格式结果
print(res.headers)#请求头
print(res.status_code)#状态码
print(res.text)#文本格式