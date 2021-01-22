def login(loginName,passWord):
    if loginName!=None and passWord!=None:
        if loginName=='yt' and passWord=='96e79218965eb72c92a549dd5a330112':
            return {'message':'Success'}
        else:
            return {'message':'用户名密码错误!'}
    return {'message':'账号或密码为空'}#账号或密码为空