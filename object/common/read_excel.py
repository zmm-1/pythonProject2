import pandas as pd
# df=pd.read_excel('case_v1.xlsx',sheet_name='login')#指定sheet表单，可以同时指定多个['sheet1','sheet2',2](结合索引)
# print(df.head())#默认第一个表单二维矩阵,当指定多个sheet时步能用head()方法
# print(df.values())#指定多个表单时用values()
# print(df.iloc[0].values)#获取第一行，不包含标题
# print(df.iloc[[0,1,3]].values)#获取多行，不包含标题
# print(df.iloc[0,0])#获取指定行列的值
# print(df.index.values)#获取所有行号
# print(df.columns.values)#获取标题
# print(df.sample(1).values)#获取指定行数的值，类似head(),.values
# print(df['data'].values)#根据标题获取列值
class ExcelMethod:
    def __init__(self, filepath):
        self.filepath = filepath
    def get_case(self,sheet):
        df = pd.read_excel(self.filepath, sheet_name=sheet,keep_default_na=False)#keep_default_na=False空值为nan的处理
        data = []
        for i in df.index.values:#获取所有行号
            title = df.columns.values#获取标题
            test_data = {}
            for x, k in enumerate(df.iloc[i].values):#获取每一行的索引与值
                test_data[title[x]] = k#添加到字典
            data.append(test_data)#添加到列表
        return data


