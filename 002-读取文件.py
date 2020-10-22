import pandas as pd

newTop = pd.read_excel('./testExcel/002-高企.xls')

# 打印它的形状 ----> （646行，11列）
print(newTop.shape)
# 打印表头行
print(newTop.columns)
# 打印前几行（默认5行）
print(newTop.head(8))
# 打印末尾几行（默认5行）
print(newTop.tail(3))
print('=========================')

newTop2 = pd.read_excel('./testExcel/002-高企-copy.xls')
# 打印表头行
print(newTop2.columns)
# 设置标题行从哪里开始
newTop2 = pd.read_excel('./testExcel/002-高企-copy.xls', header=1)
# 打印表头行
print(newTop2.columns)
print(newTop.head(3))
# 设置index列
newTop2 = pd.read_excel('./testExcel/002-高企-copy.xls', header=1, index_col='序号')
# 打印表头行
print(newTop2.columns)
print(newTop.head(3))