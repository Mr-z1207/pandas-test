import pandas as pd
from datetime import date, timedelta


# 月份累加小算法
def monAdd(startDate, num):
    hasYear = num // 12
    hasMon = startDate.month + num % 12
    if hasMon != 12:
        hasYear += hasMon // 12
        hasMon %= 12
    return date(startDate.year + hasYear, hasMon, startDate.day)


books = pd.read_excel("./testExcel/004.xlsx", skiprows=3, usecols="C:F",
                      dtype={"ID": str, "inStore": str, "Date": str})

startDate = date(2020, 1, 1)
for i in books.index:
    # 日 +1
    # books["Date"].at[i] = startDate + timedelta(days=i)
    # 年 +1
    # books["Date"].at[i] = date(startDate.year + i, startDate.month, startDate.day)
    # 月 +1
    books["Date"].at[i] = monAdd(startDate, i)

print(books["Date"])
