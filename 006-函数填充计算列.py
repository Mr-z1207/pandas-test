import pandas as pd

books = pd.read_excel('./testExcel/006-函数填充计算列.xlsx', index_col='ID')

# books['单价'] = books['原价'] * books['折扣']

# 只计算某一段单元格
for i in books.index:
    if 3 < i < 10:
        books['单价'].at[i] = books['原价'].at[i] * books['折扣'].at[i]
print(books)
