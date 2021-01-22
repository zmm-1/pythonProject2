import pandas as pd
import pprint
#
# df=pd.read_excel('case_v1.xlsx',sheet_name='login',keep_default_na=False)  # keep_default_na=False空值为nan的处理
# data = []
# for i in df.index.values:  # 获取所有行号
#     title = df.columns.values  # 获取标题
#     test_data = {}
#     for x, k in enumerate(df.iloc[i].values):  # 获取每一行的索引与值
#         test_data[title[x]] = k  # 添加到字典
#     data.append(test_data)  # 添加到列表
# pprint.pprint(data)


df=pd.read_excel('case_v1.xlsx',sheet_name='Sheet1',keep_default_na=False)# keep_default_na=False空值为nan的处理
print(df.to_dict(orient='records'))
# print(df.to_dict(orient='list'))
# pprint.pprint(df.to_dict(orient='split'))
# print(df.to_dict(orient='dict'))
# print(df.to_dict(orient='index'))