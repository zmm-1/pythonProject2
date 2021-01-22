
import requests

#上传文件
img_url='http://tpad.api.zjxk12.com/zjx/api/user/modifyHeadImg'
token=r'rNtq3i3wG4MKy1rZ1R1DMfVdncXaw3H4bsxDOb/neUKL5gJnfJnS69nUUC/GCxXzrOiKZ1r8lkXMI4PsTKF1Ug=='

res=requests.post(url=img_url,headers={'token':token},
                 files={'file':'D:\pythonProject2\object\data\img.png'})#文件路径

print(res.json())