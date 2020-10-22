import pandas as pd

# DataFrame一个类，参数可以是数据列表
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ami', 'Anny', 'Tom']})
# DataFrame会在首列生成一个默认的索引
print('默认的索引')
print(df)
# 可以用set_index设置ID列为索引列（这会生成一个新的df）
df = df.set_index('ID')
print('设置后的索引')
print(df)
# 生成.xlsx到本地磁盘
df.to_excel('D:/CodeBase/python/excelTest/testExcel/001test.xlsx')

print('Done!')
