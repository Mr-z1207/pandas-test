import pandas as pd

# skiprows=3 跳过前三行; usecols="C:F" 使用C-F列;
# index_col="ID"先不设置ID列，否则填充时不好操作
books = pd.read_excel("./testExcel/004.xlsx", skiprows=3, usecols="C:F",
                      dtype={"ID": str, "inStore": str, "Date": str})  # 设置列格式，这样就不是浮点数了
# 如果一开始设置了int格式，NaN的地方会报错，因为NaN无法强制转换成int格式
print(books["ID"])
# 类型为Series
print(type(books["ID"]))
# Series有一个at方法，设置单元格值
books["ID"].at[0] = 100
print(books["ID"])
# 既然能设置一个值，就能用循环设置一堆值
for i in books.index:
    books["ID"].at[i] = i + 1
    books["inStore"].at[i] = "Yes" if i%2==0 else "No"

print(books)  # 如果不设置格式，ID列数据被填充成float类型，因为之前是NaN
