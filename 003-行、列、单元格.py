import pandas as pd

# series,序列,类似于字典
dic = {'x': 100, 'Y': 200, 'z': 300}
print(dic.keys())
print(dic.values())
print(dic['x'])
print('=====================')

# 把dict变成series
s1 = pd.Series(dic)
print(s1)
print(s1.index)
print(s1.values)
print(s1['x'])
print('=====================')

# 分别定义series的index、value
L1 = [100, 200, 300]
L2 = ['x', 'y', 'z']
s2 = pd.Series(L1, index=L2)
print(s2)
print(s2.index)
print(s2.values)
print(s2['x'])
print('=====================')

# 目标表格003-01Col.xlsx
# 10  100  1000
# 20  200  2000
# 30  300  3000
# 序列既可以作为行，也可以作为列
# 作为列，要以dict的形式生成df
sCol1 = pd.Series([10, 20, 30], index=[1, 2, 3], name='A')
sCol2 = pd.Series([100, 200, 300], index=[1, 2, 3], name='B')
sCol3 = pd.Series([1000, 2000, 3000], index=[1, 2, 3], name='C')
df1 = pd.DataFrame({sCol1.name: sCol1, sCol2.name: sCol2, sCol3.name: sCol3})
print(df1)

# 作为列，要以list的形式生成df
df2 = pd.DataFrame([sCol1, sCol2, sCol3])
print(df2)

# index作用，将Series的index，对其到DataFrame的index
sCol4 = pd.Series([111, 222, 333], index=[2, 3, 4], name='D')
df3 = pd.DataFrame({sCol1.name: sCol1, sCol2.name: sCol2, sCol4.name: sCol4})
print(df3)