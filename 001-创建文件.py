import pandas as pd

# DataFrame一个类，参数可以是数据列表
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ami', 'Anny', 'Tom']})
# DataFrame会在首列生成一个默认的索引
print('默认的索引')
print(df)
# 可以用set_index设置ID列为索引列（这会生成一个新的df）
# inplace参数的作用是：是否在原对象基础上进行修改;True：不创建新的对象，直接对原始对象进行修改
df = df.set_index('ID', inplace=False)
print('设置后的索引')
print(df)
# 生成.xlsx到本地磁盘
df.to_excel('./testExcel/001test.xlsx')

print('Done!')
