import pandas as pd

#指定sheet表单，不指定表单情况下默认读取第一个表单的数据
df=pd.read_excel('case_v1.xlsx',sheet_name='Sheet1')
# #指定多个表单
# df=pd.read_excel('case_v1.xlsx',sheet_name=['login','checkRegister'])
# #通过索引指定表单
# df=pd.read_excel('case_v1.xlsx',sheet_name=1)

#根据索引获取指定行的值
print(df.iloc[0].values)#获取第一行，不包含标题
print(df.iloc[[0,1,3]].values)#获取多行，不包含标题

#获取指定单元格的值，通过横向索引与竖向索引
print(df.iloc[0,0])

#获取所有行号
print(df.index.values)

#获取标题
print(df.columns.values)

#通过标题获取列值
print(df['data'].values)#根据标题获取列值

